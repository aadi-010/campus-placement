import json
from datetime import datetime
from app.extensions import db

class InterviewQuestion(db.Model):
    __tablename__ = 'interview_questions'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False, index=True) # Technical, HR & Behavioral
    subtopic = db.Column(db.String(60), nullable=False, index=True) # OOP, DBMS, OS, Networks, Behavioral, etc.
    difficulty = db.Column(db.String(20), nullable=False, default='Medium')
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    key_points_json = db.Column(db.Text, nullable=False) # list of bullet points
    common_mistakes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    progress_records = db.relationship('InterviewProgress', backref='question', lazy='dynamic')

    @property
    def key_points(self):
        try:
            return json.loads(self.key_points_json)
        except Exception:
            return []

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'subtopic': self.subtopic,
            'difficulty': self.difficulty,
            'question': self.question,
            'answer': self.answer,
            'key_points': self.key_points,
            'common_mistakes': self.common_mistakes
        }

class InterviewProgress(db.Model):
    __tablename__ = 'interview_progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('interview_questions.id', ondelete='CASCADE'), nullable=False, index=True)
    is_reviewed = db.Column(db.Boolean, default=False)
    personal_notes = db.Column(db.Text, nullable=True)
    self_rating = db.Column(db.Integer, nullable=True) # 1 to 5 stars
    reviewed_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'question_id', name='uq_user_interview_question'),
    )
