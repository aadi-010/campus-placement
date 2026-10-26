from datetime import datetime, timedelta
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models.mock_test import MockTest, MockTestAttempt, MockTestResponse
from app.models.aptitude import AptitudeQuestion

mock_tests_bp = Blueprint('mock_tests', __name__)

@mock_tests_bp.route('/')
@login_required
def index():
    tests = MockTest.query.all()
    user_attempts = MockTestAttempt.query.filter_by(
        user_id=current_user.id
    ).order_by(MockTestAttempt.started_at.desc()).all()

    return render_template('mock_tests/index.html',
        tests=tests,
        attempts=user_attempts
    )

@mock_tests_bp.route('/start/<int:test_id>', methods=['POST'])
@login_required
def start_test(test_id):
    test = MockTest.query.get_or_404(test_id)

    # Check if there is already an in_progress attempt for this test
    existing = MockTestAttempt.query.filter_by(
        user_id=current_user.id,
        mock_test_id=test.id,
        status='in_progress'
    ).first()

    now = datetime.utcnow()
    if existing:
        if existing.is_expired:
            _finalize_attempt(existing)
        else:
            return redirect(url_for('mock_tests.take_test', attempt_id=existing.id))

    # Create new attempt with strict server deadline
    deadline = now + timedelta(minutes=test.duration_minutes)
    attempt = MockTestAttempt(
        user_id=current_user.id,
        mock_test_id=test.id,
        started_at=now,
        deadline_at=deadline,
        total_questions=test.total_questions,
        status='in_progress'
    )
    db.session.add(attempt)
    db.session.flush()

    # Seed mock test responses rows for each question
    question_ids = test.question_ids
    for q_id in question_ids:
        resp = MockTestResponse(
            attempt_id=attempt.id,
            question_id=q_id,
            selected_option=None,
            is_marked_for_review=False
        )
        db.session.add(resp)

    db.session.commit()
    return redirect(url_for('mock_tests.take_test', attempt_id=attempt.id))

@mock_tests_bp.route('/take/<int:attempt_id>')
@login_required
def take_test(attempt_id):
    attempt = MockTestAttempt.query.get_or_404(attempt_id)
    if attempt.user_id != current_user.id:
        flash('Unauthorized access to mock test attempt.', 'danger')
        return redirect(url_for('mock_tests.index'))

    # Server-enforced expiry check
    if attempt.status == 'in_progress' and attempt.is_expired:
        _finalize_attempt(attempt)
        return redirect(url_for('mock_tests.view_result', attempt_id=attempt.id))

    if attempt.status != 'in_progress':
        return redirect(url_for('mock_tests.view_result', attempt_id=attempt.id))

    # Load questions without exposing correct answers
    responses = MockTestResponse.query.filter_by(attempt_id=attempt.id).all()
    questions_data = []

    for idx, r in enumerate(responses):
        q = AptitudeQuestion.query.get(r.question_id)
        if q:
            questions_data.append({
                'index': idx + 1,
                'response_id': r.id,
                'question_id': q.id,
                'category': q.category,
                'topic': q.topic,
                'difficulty': q.difficulty,
                'question': q.question,
                'options': q.options,
                'selected_option': r.selected_option,
                'is_marked': r.is_marked_for_review
            })

    return render_template('mock_tests/take.html',
        attempt=attempt,
        test=attempt.mock_test,
        questions=questions_data,
        remaining_seconds=attempt.remaining_seconds
    )

@mock_tests_bp.route('/api/<int:attempt_id>/answer', methods=['POST'])
@login_required
def record_answer_api(attempt_id):
    attempt = MockTestAttempt.query.get_or_404(attempt_id)
    if attempt.user_id != current_user.id or attempt.status != 'in_progress':
        return jsonify({'success': False, 'error': 'Invalid or closed test'}), 403

    if attempt.is_expired:
        _finalize_attempt(attempt)
        return jsonify({'success': False, 'expired': True, 'error': 'Time expired'}), 400

    data = request.get_json() or {}
    question_id = data.get('question_id')
    selected_option = data.get('selected_option') # can be None to unselect
    is_marked = data.get('is_marked')

    resp = MockTestResponse.query.filter_by(
        attempt_id=attempt.id, question_id=question_id
    ).first()

    if resp:
        if selected_option is not None:
            resp.selected_option = int(selected_option) if selected_option != '' else None
        if is_marked is not None:
            resp.is_marked_for_review = bool(is_marked)
        db.session.commit()

    return jsonify({'success': True, 'remaining_seconds': attempt.remaining_seconds})

@mock_tests_bp.route('/submit/<int:attempt_id>', methods=['POST'])
@login_required
def submit_test(attempt_id):
    attempt = MockTestAttempt.query.get_or_404(attempt_id)
    if attempt.user_id != current_user.id:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 403

    _finalize_attempt(attempt)
    return redirect(url_for('mock_tests.view_result', attempt_id=attempt.id))

@mock_tests_bp.route('/result/<int:attempt_id>')
@login_required
def view_result(attempt_id):
    attempt = MockTestAttempt.query.get_or_404(attempt_id)
    if attempt.user_id != current_user.id:
        flash('Unauthorized access to test result.', 'danger')
        return redirect(url_for('mock_tests.index'))

    # Collect answers with explanations for review
    responses = MockTestResponse.query.filter_by(attempt_id=attempt.id).all()
    review_items = []
    topic_breakdown = {}

    for idx, r in enumerate(responses):
        q = AptitudeQuestion.query.get(r.question_id)
        if q:
            # Topic stats
            if q.topic not in topic_breakdown:
                topic_breakdown[q.topic] = {'total': 0, 'correct': 0}
            topic_breakdown[q.topic]['total'] += 1
            if r.is_correct:
                topic_breakdown[q.topic]['correct'] += 1

            review_items.append({
                'index': idx + 1,
                'question': q,
                'selected_option': r.selected_option,
                'is_correct': r.is_correct,
                'is_marked': r.is_marked_for_review
            })

    return render_template('mock_tests/result.html',
        attempt=attempt,
        test=attempt.mock_test,
        review_items=review_items,
        topic_breakdown=topic_breakdown
    )

def _finalize_attempt(attempt):
    if attempt.status != 'in_progress':
        return

    now = datetime.utcnow()
    attempt.submitted_at = min(now, attempt.deadline_at + timedelta(seconds=10))
    attempt.status = 'completed' if now <= (attempt.deadline_at + timedelta(seconds=15)) else 'expired'

    responses = MockTestResponse.query.filter_by(attempt_id=attempt.id).all()
    correct = 0
    incorrect = 0
    unattempted = 0

    for r in responses:
        q = AptitudeQuestion.query.get(r.question_id)
        if r.selected_option is None:
            unattempted += 1
            r.is_correct = False
        elif q and r.selected_option == q.correct_option:
            correct += 1
            r.is_correct = True
        else:
            incorrect += 1
            r.is_correct = False

    attempt.correct_count = correct
    attempt.incorrect_count = incorrect
    attempt.unattempted_count = unattempted
    attempt.total_questions = len(responses)

    # Score calculation: 1 mark per correct answer (standard percentage)
    if attempt.total_questions > 0:
        attempt.score = round((correct / attempt.total_questions) * 100.0, 1)
    else:
        attempt.score = 0.0

    attempt.time_spent_seconds = int((attempt.submitted_at - attempt.started_at).total_seconds())
    db.session.commit()
