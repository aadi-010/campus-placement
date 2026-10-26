from app.extensions import db
from app.models.user import User
from app.models.aptitude import AptitudeQuestion, AptitudeAttempt
from app.models.coding import CodingChallenge, CodingSubmission
from app.models.interview import InterviewQuestion, InterviewProgress
from app.models.mock_test import MockTest, MockTestAttempt
from app.services.readiness import calculate_readiness_score

def test_readiness_score_zero_for_new_user(app):
    with app.app_context():
        u = User(email='new@user.edu', full_name='Brand New')
        u.set_password('Pass@123')
        db.session.add(u)
        db.session.commit()

        score_data = calculate_readiness_score(u.id)
        assert score_data['score'] == 0
        assert score_data['aptitude']['score'] == 0
        assert score_data['coding']['score'] == 0
        assert score_data['interview']['score'] == 0
        assert score_data['mock_tests']['score'] == 0

def test_readiness_score_scales_with_verified_activity(app):
    with app.app_context():
        u = User(email='active@user.edu', full_name='Active Student')
        u.set_password('Pass@123')
        db.session.add(u)
        db.session.commit()

        # Add 10 correct aptitude attempts
        for i in range(10):
            q = AptitudeQuestion(category='Quant', topic='Math', question=f'Q{i}', options_json='["A"]', correct_option=0, explanation='E')
            db.session.add(q)
            db.session.flush()
            att = AptitudeAttempt(user_id=u.id, question_id=q.id, selected_option=0, is_correct=True)
            db.session.add(att)

        # Add 5 accepted coding challenges
        for i in range(5):
            ch = CodingChallenge(
                title=f'C{i}', slug=f'c-{i}', topic='Arrays',
                description='D', examples_json='[]', starter_code_python='print(1)',
                test_cases_json='[{"input":"", "expected_output":"1"}]'
            )
            db.session.add(ch)
            db.session.flush()
            sub = CodingSubmission(
                user_id=u.id, challenge_id=ch.id, status='Accepted',
                source_code='print(1)', passed_tests=1, total_tests=1
            )
            db.session.add(sub)

        # Add 6 reviewed interviews
        for i in range(6):
            iq = InterviewQuestion(
                category='Technical', subtopic='DBMS', difficulty='Easy',
                question=f'IQ{i}', answer='Ans', key_points_json='["P1"]'
            )
            db.session.add(iq)
            db.session.flush()
            ip = InterviewProgress(user_id=u.id, question_id=iq.id, is_reviewed=True)
            db.session.add(ip)

        db.session.commit()

        score_data = calculate_readiness_score(u.id)
        assert score_data['score'] > 0
        assert score_data['score'] <= 100
        assert score_data['aptitude']['attempted'] == 10
        assert score_data['coding']['solved'] == 5
        assert score_data['interview']['reviewed'] == 6
