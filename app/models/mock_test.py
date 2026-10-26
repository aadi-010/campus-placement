import json
from datetime import datetime, timedelta
from app.extensions import db

class MockTest(db.Model):
    __tablename__ = 'mock_tests'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(60), nullable=False, index=True) # Quantitative, Logical, Verbal, Mixed Placement
    description = db.Column(db.Text, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False, default=30)
    total_questions = db.Column(db.Integer, nullable=False, default=20)
    questions_json = db.Column(db.Text, nullable=False) # list of AptitudeQuestion IDs
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    attempts = db.relationship('MockTestAttempt', backref='mock_test', lazy='dynamic')

    @property
    def question_ids(self):
        try:
            return json.loads(self.questions_json)
        except Exception:
            return []

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'description': self.description,
            'duration_minutes': self.duration_minutes,
            'total_questions': self.total_questions
        }

class MockTestAttempt(db.Model):
    __tablename__ = 'mock_test_attempts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    mock_test_id = db.Column(db.Integer, db.ForeignKey('mock_tests.id', ondelete='CASCADE'), nullable=False, index=True)
    started_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    deadline_at = db.Column(db.DateTime, nullable=False)
    submitted_at = db.Column(db.DateTime, nullable=True)
    score = db.Column(db.Float, default=0.0)
    total_questions = db.Column(db.Integer, default=0)
    correct_count = db.Column(db.Integer, default=0)
    incorrect_count = db.Column(db.Integer, default=0)
    unattempted_count = db.Column(db.Integer, default=0)
    time_spent_seconds = db.Column(db.Integer, default=0)
    status = db.Column(db.String(30), default='in_progress', index=True) # in_progress, completed, expired

    # Relationships
    responses = db.relationship('MockTestResponse', backref='attempt', lazy='dynamic', cascade='all, delete-orphan')

    @property
    def is_expired(self):
        if self.status != 'in_progress':
            return False
        # Add a 15-second grace period for network transit
        return datetime.utcnow() > (self.deadline_at + timedelta(seconds=15))

    @property
    def remaining_seconds(self):
        if self.status != 'in_progress':
            return 0
        rem = (self.deadline_at - datetime.utcnow()).total_seconds()
        return max(0, int(rem))

class MockTestResponse(db.Model):
    __tablename__ = 'mock_test_responses'

    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('mock_test_attempts.id', ondelete='CASCADE'), nullable=False, index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('aptitude_questions.id', ondelete='CASCADE'), nullable=False)
    selected_option = db.Column(db.Integer, nullable=True) # None if unattempted, or 0, 1, 2, 3
    is_marked_for_review = db.Column(db.Boolean, default=False)
    is_correct = db.Column(db.Boolean, default=False)

    __table_args__ = (
        db.UniqueConstraint('attempt_id', 'question_id', name='uq_attempt_question_response'),
    )
