"""
Placement Readiness Score Calculator
Formula and transparent weights:
1. Aptitude Performance (30% total):
   - Unique questions attempted vs target (15%)
   - Accuracy rate on unique attempted questions (15%)
2. Coding Challenges (30% total):
   - Unique challenges solved vs minimum benchmark (20%)
   - Success rate across submissions (10%)
3. Interview Preparation (20% total):
   - Questions reviewed and self-tested vs target (20%)
4. Mock Test Performance (20% total):
   - Completed mock tests (10%)
   - Average score across completed mock tests (10%)

Total Score: 0% to 100%
Note: This is an estimated practice readiness benchmark to guide self-study.
"""
from sqlalchemy import func
from app.models.aptitude import AptitudeAttempt, AptitudeQuestion
from app.models.coding import CodingSubmission, CodingChallenge
from app.models.interview import InterviewProgress, InterviewQuestion
from app.models.mock_test import MockTestAttempt

from app.extensions import db

def calculate_readiness_score(user_id):
    # 1. Aptitude metrics
    # Unique questions attempted
    unique_aptitude_attempts = AptitudeAttempt.query.filter_by(user_id=user_id)\
        .with_entities(
            AptitudeAttempt.question_id,
            func.max(db.case((AptitudeAttempt.is_correct == True, 1), else_=0))
        )\
        .group_by(AptitudeAttempt.question_id).all()

    total_attempted_aptitude = len(unique_aptitude_attempts)
    correct_unique_aptitude = sum(1 for _, is_corr in unique_aptitude_attempts if is_corr == 1)
    
    aptitude_accuracy = (correct_unique_aptitude / total_attempted_aptitude) if total_attempted_aptitude > 0 else 0
    # Benchmark target: 50 unique questions
    aptitude_volume_score = min(1.0, total_attempted_aptitude / 50.0) * 15.0
    aptitude_accuracy_score = (aptitude_accuracy * 15.0)
    aptitude_total = aptitude_volume_score + aptitude_accuracy_score

    # 2. Coding metrics
    # Unique challenges solved (status == 'Accepted')
    solved_challenges = CodingSubmission.query.filter_by(user_id=user_id, status='Accepted')\
        .with_entities(CodingSubmission.challenge_id).distinct().count()
    
    total_challenges_count = max(1, CodingChallenge.query.count())
    coding_volume_score = min(1.0, solved_challenges / 20.0) * 20.0
    
    all_submissions_count = CodingSubmission.query.filter_by(user_id=user_id).count()
    accepted_submissions_count = CodingSubmission.query.filter_by(user_id=user_id, status='Accepted').count()
    coding_accuracy = (accepted_submissions_count / all_submissions_count) if all_submissions_count > 0 else 0
    coding_accuracy_score = coding_accuracy * 10.0
    coding_total = coding_volume_score + coding_accuracy_score

    # 3. Interview metrics
    reviewed_interviews = InterviewProgress.query.filter_by(user_id=user_id, is_reviewed=True).count()
    # Benchmark target: 30 questions reviewed
    interview_total = min(1.0, reviewed_interviews / 30.0) * 20.0

    # 4. Mock test metrics
    completed_mock_tests = MockTestAttempt.query.filter_by(user_id=user_id, status='completed').all()
    mock_volume_score = min(1.0, len(completed_mock_tests) / 5.0) * 10.0
    
    if completed_mock_tests:
        avg_score = sum(t.score for t in completed_mock_tests) / len(completed_mock_tests)
        mock_score_score = (min(100.0, avg_score) / 100.0) * 10.0
    else:
        mock_score_score = 0.0
    
    mock_total = mock_volume_score + mock_score_score

    # Final readiness percentage
    overall_score = round(aptitude_total + coding_total + interview_total + mock_total)
    overall_score = max(0, min(100, overall_score))

    breakdown = {
        'score': overall_score,
        'overall_score': overall_score,
        'aptitude': {
            'score': round(aptitude_total, 1),
            'max': 30,
            'attempted': total_attempted_aptitude,
            'accuracy': round(aptitude_accuracy * 100, 1)
        },
        'coding': {
            'score': round(coding_total, 1),
            'max': 30,
            'solved': solved_challenges,
            'submissions': all_submissions_count
        },
        'interview': {
            'score': round(interview_total, 1),
            'max': 20,
            'reviewed': reviewed_interviews
        },
        'mock_tests': {
            'score': round(mock_total, 1),
            'max': 20,
            'completed': len(completed_mock_tests),
            'avg_score': round(sum(t.score for t in completed_mock_tests) / len(completed_mock_tests), 1) if completed_mock_tests else 0
        },
        'breakdown': {
            'aptitude': {
                'earned_points': round(aptitude_total, 1),
                'unique_answered': total_attempted_aptitude
            },
            'coding': {
                'earned_points': round(coding_total, 1),
                'unique_solved': solved_challenges
            },
            'interview': {
                'earned_points': round(interview_total, 1),
                'unique_reviewed': reviewed_interviews
            },
            'mock_tests': {
                'earned_points': round(mock_total, 1),
                'attempts_count': len(completed_mock_tests)
            }
        }
    }

    return breakdown
