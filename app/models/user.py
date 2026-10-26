from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    college = db.Column(db.String(180), nullable=True)
    graduation_year = db.Column(db.Integer, nullable=True)
    target_role = db.Column(db.String(120), nullable=True)
    daily_goal = db.Column(db.Integer, default=10)
    current_streak = db.Column(db.Integer, default=1)
    last_active_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    aptitude_attempts = db.relationship('AptitudeAttempt', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    coding_submissions = db.relationship('CodingSubmission', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    coding_drafts = db.relationship('CodingDraft', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    interview_progress = db.relationship('InterviewProgress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    mock_test_attempts = db.relationship('MockTestAttempt', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    bookmarks = db.relationship('Bookmark', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'college': self.college or '',
            'graduation_year': self.graduation_year or '',
            'target_role': self.target_role or 'Software Engineer',
            'daily_goal': self.daily_goal,
            'current_streak': self.current_streak,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
