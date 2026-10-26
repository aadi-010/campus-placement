import pytest
from app.extensions import db
from app.models.user import User
from app.models.coding import CodingChallenge, CodingSubmission

def test_progress_dashboard_renders_successfully(client, app):
    with app.app_context():
        u = User(email='progress_user@campusprep.edu', full_name='Progress User')
        u.set_password('Secret123!')
        db.session.add(u)
        
        # Add a sample coding challenge and submission to populate coding_stats
        c = CodingChallenge(
            title='Two Sum Progress',
            slug='two-sum-progress',
            topic='Arrays',
            difficulty='Easy',
            description='Test challenge',
            examples_json='[]',
            starter_code_python='def solve(): pass',
            test_cases_json='[{"input":"1", "expected_output":"1"}]'
        )
        db.session.add(c)
        db.session.commit()

        sub = CodingSubmission(
            user_id=u.id,
            challenge_id=c.id,
            status='Accepted',
            source_code='def solve(): pass',
            passed_tests=1,
            total_tests=1
        )
        db.session.add(sub)
        db.session.commit()

    # Log in
    client.post('/auth/login', data={
        'email': 'progress_user@campusprep.edu',
        'password': 'Secret123!'
    }, follow_redirects=True)

    # Access /progress/
    response = client.get('/progress/')
    assert response.status_code == 200
    assert b'Placement Readiness' in response.data
    assert b'Coding Challenges Solved' in response.data

    # Access /progress/api/chart-data
    api_res = client.get('/progress/api/chart-data')
    assert api_res.status_code == 200
    data = api_res.get_json()
    assert data['success'] is True
    assert 'mock_tests' in data
