"""
Vercel Serverless Function entry point for CampusPrep Flask application.
Exposes 'app' WSGI application and ensures database tables/seeds are ready on cold starts.
"""
import os
import sys

# Ensure root repository directory is on sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app import create_app
from app.extensions import db

# Determine environment (production by default on Vercel)
config_env = os.environ.get('FLASK_ENV', 'production')
app = create_app(config_env)

# Ensure database tables and initial seed data exist on serverless cold starts
with app.app_context():
    try:
        db.create_all()
        from app.models.aptitude import AptitudeQuestion
        if AptitudeQuestion.query.first() is None:
            from scripts.seed import seed_database
            seed_database(app=app)
    except Exception as exc:
        app.logger.warning(f"Serverless DB cold start notice: {exc}")
