import json
from datetime import datetime
from app.extensions import db

class CodingChallenge(db.Model):
    __tablename__ = 'coding_challenges'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False, index=True)
    topic = db.Column(db.String(60), nullable=False, index=True) # Arrays, Strings, Trees, DP, etc.
    difficulty = db.Column(db.String(20), nullable=False, default='Easy', index=True) # Easy, Medium, Hard
    description = db.Column(db.Text, nullable=False)
    constraints = db.Column(db.Text, nullable=True)
    examples_json = db.Column(db.Text, nullable=False) # list of {input, output, explanation}
    hints_json = db.Column(db.Text, nullable=True) # list of hints
    test_cases_json = db.Column(db.Text, nullable=False) # list of {input, expected_output, is_hidden}
    starter_code_python = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    submissions = db.relationship('CodingSubmission', backref='challenge', lazy='dynamic')
    drafts = db.relationship('CodingDraft', backref='challenge', lazy='dynamic')

    @property
    def examples(self):
        try:
            return json.loads(self.examples_json)
        except Exception:
            return []

    @property
    def hints(self):
        try:
            return json.loads(self.hints_json) if self.hints_json else []
        except Exception:
            return []

    @property
    def test_cases(self):
        try:
            return json.loads(self.test_cases_json)
        except Exception:
            return []

    def to_dict(self, include_test_cases=False):
        data = {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'topic': self.topic,
            'difficulty': self.difficulty,
            'description': self.description,
            'constraints': self.constraints,
            'examples': self.examples,
            'hints': self.hints,
            'starter_code_python': self.starter_code_python
        }
        if include_test_cases:
            data['test_cases'] = [tc for tc in self.test_cases if not tc.get('is_hidden', False)]
        return data

class CodingSubmission(db.Model):
    __tablename__ = 'coding_submissions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    challenge_id = db.Column(db.Integer, db.ForeignKey('coding_challenges.id', ondelete='CASCADE'), nullable=False, index=True)
    language = db.Column(db.String(30), default='python')
    source_code = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(40), nullable=False) # 'Accepted', 'Wrong Answer', 'Syntax Error', 'Time Limit Exceeded', 'Practice Saved'
    execution_time_ms = db.Column(db.Integer, default=0)
    passed_tests = db.Column(db.Integer, default=0)
    total_tests = db.Column(db.Integer, default=0)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

class CodingDraft(db.Model):
    __tablename__ = 'coding_drafts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    challenge_id = db.Column(db.Integer, db.ForeignKey('coding_challenges.id', ondelete='CASCADE'), nullable=False, index=True)
    source_code = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'challenge_id', name='uq_user_challenge_draft'),
    )
