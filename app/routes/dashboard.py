from datetime import datetime, date
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy import func
from app.extensions import db
from app.models.aptitude import AptitudeAttempt, AptitudeQuestion
from app.models.coding import CodingSubmission, CodingChallenge
from app.models.interview import InterviewProgress, InterviewQuestion
from app.models.mock_test import MockTestAttempt
from app.services.readiness import calculate_readiness_score

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    user_id = current_user.id

    # 1. Update streak if needed
    today = date.today()
    if current_user.last_active_date != today:
        if current_user.last_active_date and (today - current_user.last_active_date).days == 1:
            current_user.current_streak += 1
        elif not current_user.last_active_date:
            current_user.current_streak = 1
        current_user.last_active_date = today
        db.session.commit()

    # 2. Live Database Statistics
    aptitude_attempted_count = AptitudeAttempt.query.filter_by(user_id=user_id)\
        .with_entities(AptitudeAttempt.question_id).distinct().count()

    coding_solved_count = CodingSubmission.query.filter_by(user_id=user_id, status='Accepted')\
        .with_entities(CodingSubmission.challenge_id).distinct().count()

    interview_reviewed_count = InterviewProgress.query.filter_by(user_id=user_id, is_reviewed=True).count()

    completed_mock_tests = MockTestAttempt.query.filter_by(user_id=user_id, status='completed').all()
    avg_mock_score = round(sum(t.score for t in completed_mock_tests) / len(completed_mock_tests), 1) if completed_mock_tests else 0.0

    # 3. Placement Readiness Calculation
    readiness = calculate_readiness_score(user_id)

    # 4. Daily practice count today
    today_start = datetime.combine(today, datetime.min.time())
    today_aptitude = AptitudeAttempt.query.filter(
        AptitudeAttempt.user_id == user_id,
        AptitudeAttempt.attempted_at >= today_start
    ).count()
    today_coding = CodingSubmission.query.filter(
        CodingSubmission.user_id == user_id,
        CodingSubmission.submitted_at >= today_start
    ).count()
    today_progress_total = today_aptitude + today_coding
    daily_goal = current_user.daily_goal or 10
    daily_percentage = min(100, int((today_progress_total / daily_goal) * 100))

    # 5. Recent Activity Feed
    recent_aptitude = AptitudeAttempt.query.filter_by(user_id=user_id)\
        .order_by(AptitudeAttempt.attempted_at.desc()).limit(3).all()
    recent_coding = CodingSubmission.query.filter_by(user_id=user_id)\
        .order_by(CodingSubmission.submitted_at.desc()).limit(3).all()

    # 6. Weakest Topic Identification for Recommendations
    topic_stats = db.session.query(
        AptitudeQuestion.topic,
        func.count(AptitudeAttempt.id).label('total'),
        func.sum(db.case((AptitudeAttempt.is_correct == True, 1), else_=0)).label('correct')
    ).join(AptitudeAttempt, AptitudeAttempt.question_id == AptitudeQuestion.id)\
     .filter(AptitudeAttempt.user_id == user_id)\
     .group_by(AptitudeQuestion.topic).all()

    recommended_topic = "Percentages & Profit"
    lowest_acc = 100.0
    for topic, total, correct in topic_stats:
        if total >= 2:
            acc = (correct / total) * 100
            if acc < lowest_acc:
                lowest_acc = acc
                recommended_topic = topic

    return render_template('dashboard/index.html',
        aptitude_attempted_count=aptitude_attempted_count,
        coding_solved_count=coding_solved_count,
        interview_reviewed_count=interview_reviewed_count,
        avg_mock_score=avg_mock_score,
        mock_tests_taken=len(completed_mock_tests),
        readiness=readiness,
        today_progress_total=today_progress_total,
        daily_goal=daily_goal,
        daily_percentage=daily_percentage,
        recent_aptitude=recent_aptitude,
        recent_coding=recent_coding,
        recommended_topic=recommended_topic
    )
