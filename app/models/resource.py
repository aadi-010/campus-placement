from datetime import datetime
from app.extensions import db

class PlacementResource(db.Model):
    __tablename__ = 'placement_resources'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    category = db.Column(db.String(80), nullable=False, index=True) # Aptitude Notes, Coding Roadmaps, DSA Guides, Resume, Interview, Core CS, Git, Communication
    description = db.Column(db.Text, nullable=False)
    external_url = db.Column(db.String(300), nullable=False)
    resource_type = db.Column(db.String(50), default='Guide') # Article, Interactive, Documentation, Roadmap, Video
    estimated_time = db.Column(db.String(50), default='15 mins')
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'description': self.description,
            'external_url': self.external_url,
            'resource_type': self.resource_type,
            'estimated_time': self.estimated_time,
            'is_featured': self.is_featured
        }
