from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy import func
from app.extensions import db
from app.models.interview import InterviewQuestion, InterviewProgress
from app.models.aptitude import Bookmark

interviews_bp = Blueprint('interviews', __name__)

@interviews_bp.route('/')
@login_required
def index():
    category = request.args.get('category', 'all')
    subtopic = request.args.get('subtopic', 'all')
    search = request.args.get('search', '').strip()

    query = InterviewQuestion.query

    if category != 'all':
        query = query.filter(InterviewQuestion.category == category)
    if subtopic != 'all':
        query = query.filter(InterviewQuestion.subtopic == subtopic)
    if search:
        query = query.filter(
            (InterviewQuestion.question.ilike(f'%{search}%')) |
            (InterviewQuestion.subtopic.ilike(f'%{search}%'))
        )

    questions = query.order_by(InterviewQuestion.id).all()

    # User progress dict: question_id -> InterviewProgress
    progress_records = {
        p.question_id: p for p in InterviewProgress.query.filter_by(user_id=current_user.id).all()
    }

    # Bookmarks
    bookmarks = set(b.item_id for b in Bookmark.query.filter_by(
        user_id=current_user.id, item_type='interview'
    ).all())

    categories = [r[0] for r in db.session.query(InterviewQuestion.category).distinct().all()]
    subtopics = [r[0] for r in db.session.query(InterviewQuestion.subtopic).distinct().order_by(InterviewQuestion.subtopic).all()]

    return render_template('interview/index.html',
        questions=questions,
        progress_records=progress_records,
        bookmarks=bookmarks,
        categories=categories,
        subtopics=subtopics,
        selected_category=category,
        selected_subtopic=subtopic,
        search_query=search,
        total_count=len(questions)
    )

@interviews_bp.route('/practice')
@login_required
def practice():
    category = request.args.get('category', 'all')
    question_id = request.args.get('id', type=int)

    query = InterviewQuestion.query
    if category != 'all':
        query = query.filter(InterviewQuestion.category == category)
    
    if question_id:
        question = InterviewQuestion.query.get_or_404(question_id)
    else:
        question = query.order_by(func.random()).first()

    progress = None
    if question:
        progress = InterviewProgress.query.filter_by(
            user_id=current_user.id, question_id=question.id
        ).first()

    return render_template('interview/practice.html',
        question=question,
        progress=progress,
        selected_category=category
    )

@interviews_bp.route('/api/review', methods=['POST'])
@login_required
def save_review_api():
    data = request.get_json() or {}
    question_id = data.get('question_id')
    is_reviewed = data.get('is_reviewed', True)
    personal_notes = data.get('personal_notes')
    self_rating = data.get('self_rating')

    progress = InterviewProgress.query.filter_by(
        user_id=current_user.id, question_id=question_id
    ).first()

    if progress:
        progress.is_reviewed = bool(is_reviewed)
        if personal_notes is not None:
            progress.personal_notes = personal_notes
        if self_rating is not None:
            progress.self_rating = int(self_rating)
    else:
        progress = InterviewProgress(
            user_id=current_user.id,
            question_id=question_id,
            is_reviewed=bool(is_reviewed),
            personal_notes=personal_notes or None,
            self_rating=int(self_rating) if self_rating else None
        )
        db.session.add(progress)

    db.session.commit()
    return jsonify({'success': True, 'is_reviewed': progress.is_reviewed})
