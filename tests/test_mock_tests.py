import json
from datetime import datetime, timedelta
from app.extensions import db
from app.models.aptitude import AptitudeQuestion
from app.models.mock_test import MockTest, MockTestAttempt, MockTestResponse

def test_mock_test_start_and_deadline_enforcement(auth_client, app):
    with app.app_context():
        # Create a mock test with 2 questions
        q1 = AptitudeQuestion(category='Quantitative', topic='Ratios', question='Q1', options_json='["A","B"]', correct_option=0, explanation='E1')
        q2 = AptitudeQuestion(category='Quantitative', topic='Ratios', question='Q2', options_json='["A","B"]', correct_option=1, explanation='E2')
        db.session.add_all([q1, q2])
        db.session.commit()

        test = MockTest(
            title='Quick Assessment',
            category='Quantitative',
            description='Test description',
            duration_minutes=20,
            total_questions=2,
            questions_json=json.dumps([q1.id, q2.id])
        )
        db.session.add(test)
        db.session.commit()
        test_id = test.id

    # Start test
    res = auth_client.post(f'/mock-tests/start/{test_id}', follow_redirects=False)
    assert res.status_code == 302
    assert '/mock-tests/take/' in res.headers['Location']

    with app.app_context():
        attempt = MockTestAttempt.query.filter_by(mock_test_id=test_id).first()
        assert attempt is not None
        assert attempt.status == 'in_progress'
        # Check deadline is roughly 20 mins from start
        diff = (attempt.deadline_at - attempt.started_at).total_seconds()
        assert 1190 <= diff <= 1210
        assert attempt.is_expired is False

def test_mock_test_answer_submission_and_scoring(auth_client, app):
    with app.app_context():
        q1 = AptitudeQuestion(category='Quant', topic='Math', question='Q1', options_json='["A","B"]', correct_option=0, explanation='E1')
        q2 = AptitudeQuestion(category='Quant', topic='Math', question='Q2', options_json='["A","B"]', correct_option=1, explanation='E2')
        db.session.add_all([q1, q2])
        db.session.commit()

        test = MockTest(
            title='Score Assessment',
            category='Quantitative',
            description='Test',
            duration_minutes=15,
            total_questions=2,
            questions_json=json.dumps([q1.id, q2.id])
        )
        db.session.add(test)
        db.session.commit()
        test_id = test.id
        q1_id = q1.id
        q2_id = q2.id

    # Start test
    auth_client.post(f'/mock-tests/start/{test_id}', follow_redirects=True)

    with app.app_context():
        attempt = MockTestAttempt.query.filter_by(mock_test_id=test_id).first()
        att_id = attempt.id

    # Answer Q1 correctly (option 0)
    res_ans1 = auth_client.post(f'/mock-tests/api/{att_id}/answer', json={
        'question_id': q1_id,
        'selected_option': 0
    })
    assert res_ans1.status_code == 200
    assert res_ans1.get_json()['success'] is True

    # Answer Q2 incorrectly (option 0 instead of 1)
    res_ans2 = auth_client.post(f'/mock-tests/api/{att_id}/answer', json={
        'question_id': q2_id,
        'selected_option': 0
    })
    assert res_ans2.status_code == 200

    # Submit test
    res_sub = auth_client.post(f'/mock-tests/submit/{att_id}', follow_redirects=True)
    assert res_sub.status_code == 200

    with app.app_context():
        attempt = MockTestAttempt.query.get(att_id)
        assert attempt.status == 'completed'
        assert attempt.correct_count == 1
        assert attempt.incorrect_count == 1
        assert attempt.score == 50.0 # 1 out of 2 = 50%
