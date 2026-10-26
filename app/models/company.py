import json
from app.extensions import db

class CompanyTrack(db.Model):
    __tablename__ = 'company_tracks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False, index=True)
    tier = db.Column(db.String(50), default='Service-Based') # 'Product-Based', 'Service-Based', 'Tech Giant'
    overview = db.Column(db.Text, nullable=False)
    recruitment_stages_json = db.Column(db.Text, nullable=False) # list of {stage, name, description}
    skill_areas_json = db.Column(db.Text, nullable=False) # list of skill tags
    aptitude_topics_json = db.Column(db.Text, nullable=False) # list of topics
    coding_topics_json = db.Column(db.Text, nullable=False) # list of topics
    technical_topics_json = db.Column(db.Text, nullable=False) # list of topics
    hr_topics_json = db.Column(db.Text, nullable=False) # list of topics
    checklist_items_json = db.Column(db.Text, nullable=False) # list of checklist task strings
    recommended_resources_json = db.Column(db.Text, nullable=True)

    @property
    def recruitment_stages(self):
        try:
            return json.loads(self.recruitment_stages_json)
        except Exception:
            return []

    @property
    def skill_areas(self):
        try:
            return json.loads(self.skill_areas_json)
        except Exception:
            return []

    @property
    def checklist_items(self):
        try:
            return json.loads(self.checklist_items_json)
        except Exception:
            return []

    @property
    def aptitude_topics(self):
        try:
            return json.loads(self.aptitude_topics_json)
        except Exception:
            return []

    @property
    def coding_topics(self):
        try:
            return json.loads(self.coding_topics_json)
        except Exception:
            return []

    @property
    def technical_topics(self):
        try:
            return json.loads(self.technical_topics_json)
        except Exception:
            return []

    @property
    def hr_topics(self):
        try:
            return json.loads(self.hr_topics_json)
        except Exception:
            return []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'tier': self.tier,
            'overview': self.overview,
            'recruitment_stages': self.recruitment_stages,
            'skill_areas': self.skill_areas,
            'aptitude_topics': self.aptitude_topics,
            'coding_topics': self.coding_topics,
            'technical_topics': self.technical_topics,
            'hr_topics': self.hr_topics,
            'checklist_items': self.checklist_items
        }

class CompanyChecklist(db.Model):
    __tablename__ = 'company_checklists'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company_tracks.id', ondelete='CASCADE'), nullable=False, index=True)
    item_index = db.Column(db.Integer, nullable=False) # index of item in company.checklist_items
    is_completed = db.Column(db.Boolean, default=False)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'company_id', 'item_index', name='uq_user_company_checklist_item'),
    )
