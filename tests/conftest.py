import pytest
from app import create_app
from app.extensions import db
from app.models.user import User

@pytest.fixture
def app():
    app = create_app('testing')
    app.config['WTF_CSRF_ENABLED'] = False # Disable CSRF for unit testing ease
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_client(client, app):
    """Client with a logged-in student"""
    with app.app_context():
        user = User(
            email='teststudent@campusprep.edu',
            full_name='Test Student',
            college='IIT Delhi',
            graduation_year=2025,
            target_role='Software Engineer'
        )
        user.set_password('Password@123')
        db.session.add(user)
        db.session.commit()
        user_id = user.id

    # Log in through auth endpoint or session
    client.post('/auth/login', data={
        'email': 'teststudent@campusprep.edu',
        'password': 'Password@123'
    }, follow_redirects=True)

    return client
