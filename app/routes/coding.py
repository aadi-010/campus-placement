from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy import func
from app.extensions import db
from app.models.coding import CodingChallenge, CodingSubmission, CodingDraft
from app.models.aptitude import Bookmark
from app.services.code_runner import execute_python_code

coding_bp = Blueprint('coding', __name__)

@coding_bp.route('/')
@login_required
def index():
    topic = request.args.get('topic', 'all')
    difficulty = request.args.get('difficulty', 'all')
    search = request.args.get('search', '').strip()

    query = CodingChallenge.query

    if topic != 'all':
        query = query.filter(CodingChallenge.topic == topic)
    if difficulty != 'all':
        query = query.filter(CodingChallenge.difficulty == difficulty)
    if search:
        query = query.filter(
            (CodingChallenge.title.ilike(f'%{search}%')) |
            (CodingChallenge.topic.ilike(f'%{search}%'))
        )

    challenges = query.order_by(CodingChallenge.id).all()

    # Get user submission statuses
    user_submissions = CodingSubmission.query.filter_by(user_id=current_user.id).all()
    solved_set = set(s.challenge_id for s in user_submissions if s.status == 'Accepted')
    attempted_set = set(s.challenge_id for s in user_submissions)

    # Bookmarks
    bookmarks = set(b.item_id for b in Bookmark.query.filter_by(
        user_id=current_user.id, item_type='coding'
    ).all())

    topics = [r[0] for r in db.session.query(CodingChallenge.topic).distinct().order_by(CodingChallenge.topic).all()]

    return render_template('coding/index.html',
        challenges=challenges,
        solved_set=solved_set,
        attempted_set=attempted_set,
        bookmarks=bookmarks,
        topics=topics,
        selected_topic=topic,
        selected_difficulty=difficulty,
        search_query=search,
        total_count=len(challenges)
    )

@coding_bp.route('/solve/<slug>')
@login_required
def solve(slug):
    challenge = CodingChallenge.query.filter_by(slug=slug).first_or_404()

    # Retrieve existing draft if any, else starter code
    draft = CodingDraft.query.filter_by(user_id=current_user.id, challenge_id=challenge.id).first()
    initial_code = draft.source_code if draft else challenge.starter_code_python

    # Retrieve user submission history for this challenge
    submissions = CodingSubmission.query.filter_by(
        user_id=current_user.id, challenge_id=challenge.id
    ).order_by(CodingSubmission.submitted_at.desc()).limit(10).all()

    is_bookmarked = Bookmark.query.filter_by(
        user_id=current_user.id, item_type='coding', item_id=challenge.id
    ).first() is not None

    return render_template('coding/solve.html',
        challenge=challenge,
        initial_code=initial_code,
        submissions=submissions,
        is_bookmarked=is_bookmarked
    )

@coding_bp.route('/api/run', methods=['POST'])
@login_required
def run_code_api():
    """
    Runs code against sample (non-hidden) test cases.
    """
    data = request.get_json() or {}
    challenge_id = data.get('challenge_id')
    source_code = data.get('source_code', '')

    challenge = CodingChallenge.query.get(challenge_id)
    if not challenge:
        return jsonify({'success': False, 'error': 'Challenge not found'}), 404

    # Run only against public sample test cases
    sample_tests = [tc for tc in challenge.test_cases if not tc.get('is_hidden', False)]
    if not sample_tests:
        sample_tests = challenge.test_cases[:2]

    result = execute_python_code(source_code, sample_tests)
    return jsonify({'success': True, 'result': result})

@coding_bp.route('/api/submit', methods=['POST'])
@login_required
def submit_code_api():
    """
    Runs code against all test cases (including hidden) and saves official submission.
    """
    data = request.get_json() or {}
    challenge_id = data.get('challenge_id')
    source_code = data.get('source_code', '')
    language = data.get('language', 'python')

    challenge = CodingChallenge.query.get(challenge_id)
    if not challenge:
        return jsonify({'success': False, 'error': 'Challenge not found'}), 404

    # Execute against ALL test cases
    result = execute_python_code(source_code, challenge.test_cases)

    # Persist official submission
    submission = CodingSubmission(
        user_id=current_user.id,
        challenge_id=challenge.id,
        language=language,
        source_code=source_code,
        status=result['status'],
        execution_time_ms=result['execution_time_ms'],
        passed_tests=result['passed_count'],
        total_tests=result['total_count']
    )
    db.session.add(submission)

    # Also update/save draft
    draft = CodingDraft.query.filter_by(user_id=current_user.id, challenge_id=challenge.id).first()
    if draft:
        draft.source_code = source_code
    else:
        db.session.add(CodingDraft(
            user_id=current_user.id,
            challenge_id=challenge.id,
            source_code=source_code
        ))

    db.session.commit()

    return jsonify({
        'success': True,
        'result': result,
        'submission_id': submission.id,
        'status': submission.status
    })

@coding_bp.route('/api/draft', methods=['POST'])
@login_required
def save_draft_api():
    data = request.get_json() or {}
    challenge_id = data.get('challenge_id')
    source_code = data.get('source_code', '')

    draft = CodingDraft.query.filter_by(user_id=current_user.id, challenge_id=challenge_id).first()
    if draft:
        draft.source_code = source_code
    else:
        db.session.add(CodingDraft(
            user_id=current_user.id,
            challenge_id=challenge_id,
            source_code=source_code
        ))
    db.session.commit()
    return jsonify({'success': True, 'message': 'Draft saved'})
