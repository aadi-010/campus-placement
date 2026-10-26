import json
from app.extensions import db
from app.models.aptitude import AptitudeQuestion, AptitudeAttempt

def test_questions_api_does_not_expose_correct_answers(auth_client, app):
    with app.app_context():
        q = AptitudeQuestion(
            category='Quantitative Aptitude',
            topic='Percentages',
            difficulty='Easy',
            question='What is 20% of 150?',
            options_json=json.dumps(['20', '30', '40', '50']),
            correct_option=1,
            explanation='20% of 150 = 30.',
            shortcut_hint='Divide by 5'
        )
        db.session.add(q)
        db.session.commit()

    res = auth_client.get('/aptitude/api/questions?topic=Percentages')
    assert res.status_code == 200
    data = res.get_json()
    assert data['success'] is True
    assert len(data['questions']) >= 1

    first_q = data['questions'][0]
    # Ensure correct_option is NOT exposed in the questions listing API
    assert 'correct_option' not in first_q
    assert 'options' in first_q
    assert len(first_q['options']) == 4

def test_submit_answer_evaluates_correctness_and_persists(auth_client, app):
    with app.app_context():
        q = AptitudeQuestion(
            category='Quantitative Aptitude',
            topic='Percentages',
            difficulty='Easy',
            question='What is 50% of 200?',
            options_json=json.dumps(['50', '100', '150', '200']),
            correct_option=1,
            explanation='50% of 200 = 100.'
        )
        db.session.add(q)
        db.session.commit()
        q_id = q.id

    # Test Correct submission
    res = auth_client.post('/aptitude/api/submit', json={
        'question_id': q_id,
        'selected_option': 1
    })
    assert res.status_code == 200
    data = res.get_json()
    assert data['success'] is True
    assert data['is_correct'] is True
    assert data['correct_option'] == 1
    assert data['explanation'] == '50% of 200 = 100.'

    # Verify attempt in DB
    with app.app_context():
        att = AptitudeAttempt.query.filter_by(question_id=q_id).first()
        assert att is not None
        assert att.is_correct is True

    # Test Incorrect submission
    res_wrong = auth_client.post('/aptitude/api/submit', json={
        'question_id': q_id,
        'selected_option': 0
    })
    assert res_wrong.status_code == 200
    data_wrong = res_wrong.get_json()
    assert data_wrong['is_correct'] is False
