from datetime import datetime, timedelta
from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from sqlalchemy import func
from app.extensions import db
from app.models.aptitude import AptitudeAttempt, AptitudeQuestion
from app.models.coding import CodingSubmission, CodingChallenge
from app.models.interview import InterviewProgress, InterviewQuestion
from app.models.mock_test import MockTestAttempt, MockTest
from app.services.readiness import calculate_readiness_score

progress_bp = Blueprint('progress', __name__)

@progress_bp.route('/')
@login_required
def index():
    # 1. Overall Readiness
    readiness = calculate_readiness_score(current_user.id)

    # 2. Aptitude Performance by Topic
    # Query all attempts joined with questions
    attempts = db.session.query(
        AptitudeQuestion.topic,
        AptitudeAttempt.is_correct
    ).join(AptitudeAttempt, AptitudeAttempt.question_id == AptitudeQuestion.id)\
     .filter(AptitudeAttempt.user_id == current_user.id).all()

    topic_stats = {}
    for topic, is_correct in attempts:
        if topic not in topic_stats:
            topic_stats[topic] = {'total': 0, 'correct': 0}
        topic_stats[topic]['total'] += 1
        if is_correct:
            topic_stats[topic]['correct'] += 1

    topic_performance = []
    strongest_topics = []
    weakest_topics = []

    for topic, data in topic_stats.items():
        acc = int((data['correct'] / data['total']) * 100) if data['total'] > 0 else 0
        item = {
            'topic': topic,
            'total': data['total'],
            'correct': data['correct'],
            'accuracy': acc
        }
        topic_performance.append(item)
        if acc >= 70 and data['total'] >= 2:
            strongest_topics.append(item)
        elif acc < 60 and data['total'] >= 2:
            weakest_topics.append(item)

    topic_performance.sort(key=lambda x: x['total'], reverse=True)
    strongest_topics.sort(key=lambda x: x['accuracy'], reverse=True)
    weakest_topics.sort(key=lambda x: x['accuracy'])

    # 3. Coding Progress Breakdown
    coding_total = CodingChallenge.query.count()
    coding_solved_subs = db.session.query(CodingSubmission.challenge_id).filter_by(
        user_id=current_user.id, status='Accepted'
    ).distinct().all()
    solved_challenge_ids = set(c[0] for c in coding_solved_subs)
    coding_solved_count = len(solved_challenge_ids)

    # Difficulty counts
    easy_total = CodingChallenge.query.filter_by(difficulty='Easy').count()
    medium_total = CodingChallenge.query.filter_by(difficulty='Medium').count()
    hard_total = CodingChallenge.query.filter_by(difficulty='Hard').count()

    easy_solved = CodingChallenge.query.filter(
        CodingChallenge.id.in_(solved_challenge_ids),
        CodingChallenge.difficulty == 'Easy'
    ).count() if solved_challenge_ids else 0

    medium_solved = CodingChallenge.query.filter(
        CodingChallenge.id.in_(solved_challenge_ids),
        CodingChallenge.difficulty == 'Medium'
    ).count() if solved_challenge_ids else 0

    hard_solved = CodingChallenge.query.filter(
        CodingChallenge.id.in_(solved_challenge_ids),
        CodingChallenge.difficulty == 'Hard'
    ).count() if solved_challenge_ids else 0

    # 4. Interview Progress
    interview_total = InterviewQuestion.query.count()
    interview_reviewed = InterviewProgress.query.filter_by(
        user_id=current_user.id, is_reviewed=True
    ).count()

    # 5. Mock Test Attempts History
    mock_attempts = MockTestAttempt.query.filter_by(
        user_id=current_user.id, status='Completed'
    ).order_by(MockTestAttempt.submitted_at.desc()).limit(10).all()

    # 6. Weekly Activity (last 7 days count)
    today = datetime.utcnow().date()
    seven_days_ago = today - timedelta(days=6)
    
    # Generate days labels
    days = [(seven_days_ago + timedelta(days=i)) for i in range(7)]
    day_labels = [d.strftime('%a') for d in days]
    
    # Count daily aptitude attempts
    day_counts = {d.strftime('%Y-%m-%d'): 0 for d in days}
    recent_attempts = AptitudeAttempt.query.filter(
        AptitudeAttempt.user_id == current_user.id,
        AptitudeAttempt.attempted_at >= datetime.combine(seven_days_ago, datetime.min.time())
    ).all()
    for a in recent_attempts:
        k = a.attempted_at.strftime('%Y-%m-%d')
        if k in day_counts:
            day_counts[k] += 1

    activity_data = [day_counts[d.strftime('%Y-%m-%d')] for d in days]

    return render_template('dashboard/progress.html',
        readiness=readiness,
        topic_performance=topic_performance,
        strongest_topics=strongest_topics,
        weakest_topics=weakest_topics,
        coding_stats={
            'total': coding_total,
            'solved': coding_solved_count,
            'easy_total': easy_total,
            'easy_solved': easy_solved,
            'medium_total': medium_total,
            'medium_solved': medium_solved,
            'hard_total': hard_total,
            'hard_solved': hard_solved,
        },
        interview_stats={
            'total': interview_total,
            'reviewed': interview_reviewed,
            'percentage': int((interview_reviewed / interview_total) * 100) if interview_total > 0 else 0
        },
        mock_attempts=mock_attempts,
        chart_days=day_labels,
        chart_activity=activity_data
    )

@progress_bp.route('/api/chart-data')
@login_required
def api_chart_data():
    """Return JSON for dynamic chart rendering in Chart.js"""
    # 1. Mock test score trend
    mock_attempts = MockTestAttempt.query.filter_by(
        user_id=current_user.id, status='Completed'
    ).order_by(MockTestAttempt.submitted_at.asc()).all()

    mock_labels = []
    mock_scores = []
    for m in mock_attempts:
        name = m.mock_test.title if m.mock_test else 'Mock Test'
        date_str = m.submitted_at.strftime('%b %d') if m.submitted_at else ''
        mock_labels.append(f"{name} ({date_str})")
        mock_scores.append(round(m.score or 0.0, 1))

    # 2. Topic accuracy breakdown
    attempts = db.session.query(
        AptitudeQuestion.topic,
        AptitudeAttempt.is_correct
    ).join(AptitudeAttempt, AptitudeAttempt.question_id == AptitudeQuestion.id)\
     .filter(AptitudeAttempt.user_id == current_user.id).all()

    topic_stats = {}
    for topic, is_correct in attempts:
        if topic not in topic_stats:
            topic_stats[topic] = {'total': 0, 'correct': 0}
        topic_stats[topic]['total'] += 1
        if is_correct:
            topic_stats[topic]['correct'] += 1

    topic_labels = []
    topic_acc = []
    for topic, data in sorted(topic_stats.items(), key=lambda x: x[1]['total'], reverse=True)[:8]:
        topic_labels.append(topic)
        topic_acc.append(int((data['correct'] / data['total']) * 100) if data['total'] > 0 else 0)

    return jsonify({
        'success': True,
        'mock_tests': {
            'labels': mock_labels,
            'scores': mock_scores
        },
        'topics': {
            'labels': topic_labels,
            'accuracy': topic_acc
        }
    })
