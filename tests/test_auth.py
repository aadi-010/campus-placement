import pytest
from app.models.user import User

def test_register_successful(client, app):
    res = client.post('/auth/register', data={
        'full_name': 'Rohan Sharma',
        'email': 'rohan@college.edu',
        'password': 'SecurePassword@123',
        'confirm_password': 'SecurePassword@123',
        'college': 'NIT Trichy',
        'graduation_year': '2025',
        'target_role': 'Frontend Developer'
    }, follow_redirects=True)
    assert res.status_code == 200

    with app.app_context():
        user = User.query.filter_by(email='rohan@college.edu').first()
        assert user is not None
        assert user.full_name == 'Rohan Sharma'
        assert user.password_hash != 'SecurePassword@123'
        assert user.check_password('SecurePassword@123') is True

def test_duplicate_registration_rejected(client, app):
    with app.app_context():
        from app.extensions import db
        u = User(email='unique@college.edu', full_name='Original User')
        u.set_password('Password@123')
        db.session.add(u)
        db.session.commit()

    # Attempt duplicate email while unauthenticated
    res = client.post('/auth/register', data={
        'full_name': 'Duplicate User',
        'email': 'unique@college.edu',
        'password': 'Password@456',
        'confirm_password': 'Password@456'
    }, follow_redirects=True)
    assert b"already exists" in res.data

def test_login_and_logout(client, app):
    with app.app_context():
        u = User(email='alice@test.edu', full_name='Alice Wonderland')
        u.set_password('Secret@123')
        from app.extensions import db
        db.session.add(u)
        db.session.commit()

    # Login success
    login_res = client.post('/auth/login', data={
        'email': 'alice@test.edu',
        'password': 'Secret@123'
    }, follow_redirects=True)
    assert login_res.status_code == 200
    assert b"Alice Wonderland" in login_res.data or b"Dashboard" in login_res.data

    # Logout
    logout_res = client.get('/auth/logout', follow_redirects=True)
    assert logout_res.status_code == 200
    assert b"logged out safely" in logout_res.data
    # Confirm user is logged out and protected routes redirect
    dash_res = client.get('/dashboard/')
    assert dash_res.status_code == 302

def test_protected_routes_require_login(client):
    protected_urls = ['/dashboard/', '/aptitude/', '/coding/', '/interview/', '/mock-tests/', '/companies/', '/progress/']
    for url in protected_urls:
        res = client.get(url)
        assert res.status_code == 302
        assert '/auth/login' in res.headers['Location']
