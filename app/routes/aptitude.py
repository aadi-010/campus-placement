from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy import func
from app.extensions import db
from app.models.aptitude import AptitudeQuestion, AptitudeAttempt, Bookmark

aptitude_bp = Blueprint('aptitude', __name__)

@aptitude_bp.route('/')
@login_required
def index():
    category = request.args.get('category', 'all')
    topic = request.args.get('topic', 'all')
    difficulty = request.args.get('difficulty', 'all')
    search = request.args.get('search', '').strip()

    query = AptitudeQuestion.query

    if category != 'all':
        query = query.filter(AptitudeQuestion.category == category)
    if topic != 'all':
        query = query.filter(AptitudeQuestion.topic == topic)
    if difficulty != 'all':
        query = query.filter(AptitudeQuestion.difficulty == difficulty)
    if search:
        query = query.filter(
            (AptitudeQuestion.question.ilike(f'%{search}%')) |
            (AptitudeQuestion.topic.ilike(f'%{search}%'))
        )

    questions = query.order_by(AptitudeQuestion.id).all()

    # Get user attempt status for these questions
    attempted_dict = {}
    attempts = AptitudeAttempt.query.filter_by(user_id=current_user.id).all()
    for a in attempts:
        attempted_dict[a.question_id] = a.is_correct

    # Get bookmarks
    bookmarks = set(b.item_id for b in Bookmark.query.filter_by(
        user_id=current_user.id, item_type='aptitude'
    ).all())

    # Get all distinct categories and topics for filter dropdowns
    categories = [r[0] for r in db.session.query(AptitudeQuestion.category).distinct().all()]
    topics = [r[0] for r in db.session.query(AptitudeQuestion.topic).distinct().order_by(AptitudeQuestion.topic).all()]

    return render_template('aptitude/index.html',
        questions=questions,
        attempted_dict=attempted_dict,
        bookmarks=bookmarks,
        categories=categories,
        topics=topics,
        selected_category=category,
        selected_topic=topic,
        selected_difficulty=difficulty,
        search_query=search,
        total_questions=len(questions)
    )

@aptitude_bp.route('/practice')
@login_required
def practice():
    category = request.args.get('category', 'all')
    topic = request.args.get('topic', 'all')
    difficulty = request.args.get('difficulty', 'all')
    question_id = request.args.get('id', type=int)

    return render_template('aptitude/practice.html',
        initial_category=category,
        initial_topic=topic,
        initial_difficulty=difficulty,
        initial_id=question_id or ''
    )

@aptitude_bp.route('/api/questions')
@login_required
def get_questions_api():
    """
    Returns sanitized questions list WITHOUT correct options.
    """
    category = request.args.get('category', 'all')
    topic = request.args.get('topic', 'all')
    difficulty = request.args.get('difficulty', 'all')
    search = request.args.get('search', '').strip()

    query = AptitudeQuestion.query

    if category != 'all':
        query = query.filter(AptitudeQuestion.category == category)
    if topic != 'all':
        query = query.filter(AptitudeQuestion.topic == topic)
    if difficulty != 'all':
        query = query.filter(AptitudeQuestion.difficulty == difficulty)
    if search:
        query = query.filter(AptitudeQuestion.question.ilike(f'%{search}%'))

    questions = query.order_by(AptitudeQuestion.id).limit(100).all()

    # Get user bookmarks
    bookmarks = set(b.item_id for b in Bookmark.query.filter_by(
        user_id=current_user.id, item_type='aptitude'
    ).all())

    data = []
    for q in questions:
        item = q.to_public_dict()
        item['is_bookmarked'] = q.id in bookmarks
        data.append(item)

    return jsonify({'success': True, 'questions': data, 'count': len(data)})

@aptitude_bp.route('/api/submit', methods=['POST'])
@login_required
def submit_answer_api():
    """
    Backend evaluates question option submission. Never exposes correct option beforehand!
    """
    data = request.get_json() or {}
    question_id = data.get('question_id')
    selected_option = data.get('selected_option')
    time_taken = data.get('time_taken_seconds', 0)

    if question_id is None or selected_option is None:
        return jsonify({'success': False, 'error': 'Missing question_id or selected_option'}), 400

    question = AptitudeQuestion.query.get(question_id)
    if not question:
        return jsonify({'success': False, 'error': 'Question not found'}), 404

    is_correct = (int(selected_option) == question.correct_option)

    # Persist attempt in DB
    attempt = AptitudeAttempt(
        user_id=current_user.id,
        question_id=question.id,
        selected_option=int(selected_option),
        is_correct=is_correct,
        time_taken_seconds=int(time_taken)
    )
    db.session.add(attempt)
    db.session.commit()

    return jsonify({
        'success': True,
        'is_correct': is_correct,
        'correct_option': question.correct_option,
        'explanation': question.explanation,
        'shortcut_hint': question.shortcut_hint
    })
