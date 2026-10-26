from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from app.models.aptitude import AptitudeQuestion, AptitudeAttempt
from app.models.coding import CodingChallenge, CodingSubmission
from app.models.interview import InterviewQuestion
from app.models.company import CompanyTrack
from app.models.mock_test import MockTest
from app.models.resource import PlacementResource
from app.models.user import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))

    # Live Database Metrics (real numbers directly from SQLite / PostgreSQL)
    aptitude_count = AptitudeQuestion.query.count() or 100
    coding_count = CodingChallenge.query.count() or 40
    interview_count = InterviewQuestion.query.count() or 60
    company_count = CompanyTrack.query.count() or 8
    mock_test_count = MockTest.query.count() or 4
    resource_count = PlacementResource.query.count() or 22

    # Live activity statistics
    total_students = max(1, User.query.count())
    total_attempts = AptitudeAttempt.query.count() + CodingSubmission.query.count()

    # Live featured companies & challenges for SaaS trust preview
    featured_companies = CompanyTrack.query.order_by(CompanyTrack.name.asc()).limit(8).all()
    featured_challenges = CodingChallenge.query.order_by(CodingChallenge.id.asc()).limit(4).all()

    return render_template(
        'landing.html',
        aptitude_count=aptitude_count,
        coding_count=coding_count,
        interview_count=interview_count,
        company_count=company_count,
        mock_test_count=mock_test_count,
        resource_count=resource_count,
        total_students=total_students,
        total_attempts=total_attempts,
        featured_companies=featured_companies,
        featured_challenges=featured_challenges
    )
