import json
from datetime import datetime
from app.extensions import db

class AptitudeQuestion(db.Model):
    __tablename__ = 'aptitude_questions'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False, index=True) # Quantitative, Logical, Verbal
    topic = db.Column(db.String(80), nullable=False, index=True)
    difficulty = db.Column(db.String(20), nullable=False, default='Medium', index=True) # Easy, Medium, Hard
    question = db.Column(db.Text, nullable=False)
    options_json = db.Column(db.Text, nullable=False) # JSON list of 4 options
    correct_option = db.Column(db.Integer, nullable=False) # 0, 1, 2, or 3
    explanation = db.Column(db.Text, nullable=False)
    shortcut_hint = db.Column(db.Text, nullable=True)
    tags = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to attempts
    attempts = db.relationship('AptitudeAttempt', backref='question', lazy='dynamic')

    @property
    def options(self):
        try:
            return json.loads(self.options_json)
        except Exception:
            return []

    @options.setter
    def options(self, val):
        self.options_json = json.dumps(val)

    def to_public_dict(self):
        """Returns question data WITHOUT exposing the correct answer."""
        return {
            'id': self.id,
            'category': self.category,
            'topic': self.topic,
            'difficulty': self.difficulty,
            'question': self.question,
            'options': self.options,
            'shortcut_hint': self.shortcut_hint,
            'tags': self.tags.split(',') if self.tags else []
        }

    def to_full_dict(self):
        """Returns complete question including correct answer and explanation."""
        return {
            'id': self.id,
            'category': self.category,
            'topic': self.topic,
            'difficulty': self.difficulty,
            'question': self.question,
            'options': self.options,
            'correct_option': self.correct_option,
            'explanation': self.explanation,
            'shortcut_hint': self.shortcut_hint
        }

class AptitudeAttempt(db.Model):
    __tablename__ = 'aptitude_attempts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('aptitude_questions.id', ondelete='CASCADE'), nullable=False, index=True)
    selected_option = db.Column(db.Integer, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    time_taken_seconds = db.Column(db.Integer, default=0)
    attempted_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

class Bookmark(db.Model):
    __tablename__ = 'bookmarks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    item_type = db.Column(db.String(30), nullable=False) # 'aptitude', 'coding', 'interview', 'resource'
    item_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'item_type', 'item_id', name='uq_user_bookmark_item'),
    )
