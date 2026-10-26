"""
Vercel Serverless Function entry point for CampusPrep Flask application.
Exposes 'app' WSGI application with VercelPathMiddleware to handle Vercel rewrites and static files.
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

class VercelPathMiddleware:
    """
    WSGI Middleware to restore the original client request path on Vercel.
    When Vercel uses catch-all rewrites (/(.*) -> /api/index), Vercel passes
    the internal destination in PATH_INFO. This middleware extracts the client's
    actual requested path from HTTP_X_MATCHED_PATH, REQUEST_URI, or proxy headers
    and restores PATH_INFO so Flask routes and static files work correctly.
    """
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        from urllib.parse import parse_qs
        qs = parse_qs(environ.get('QUERY_STRING', ''))
        rewritten_path = qs.get('__path', [None])[0]

        if rewritten_path:
            environ['PATH_INFO'] = '/' + rewritten_path.lstrip('/')
        else:
            candidates = [
                environ.get('REQUEST_URI', ''),
                environ.get('HTTP_X_FORWARDED_PATH', ''),
                environ.get('RAW_URI', ''),
                environ.get('HTTP_X_REQUEST_URI', ''),
                environ.get('HTTP_X_MATCHED_PATH', '')
            ]
            resolved = None
            for cand in candidates:
                if cand:
                    p = cand.split('?')[0]
                    if p and not p.startswith('/api/index') and not p.startswith('/api/index.py'):
                        resolved = p
                        break
            if resolved:
                environ['PATH_INFO'] = resolved
            elif environ.get('PATH_INFO') in ('/api/index', '/api/index.py'):
                environ['PATH_INFO'] = '/'

        return self.wsgi_app(environ, start_response)

# Apply Vercel path correction middleware
app.wsgi_app = VercelPathMiddleware(app.wsgi_app)

# Fallback route handlers if /api/index is accessed directly
@app.route('/api/index')
@app.route('/api/index.py')
def vercel_entry_fallback():
    return app.view_functions['main.index']()

# Fallback route handler for static files in serverless environment
from flask import send_from_directory

@app.route('/static/<path:filename>')
def vercel_static_fallback(filename):
    static_dirs = [
        os.path.join(ROOT_DIR, 'public', 'static'),
        os.path.join(ROOT_DIR, 'app', 'static')
    ]
    for d in static_dirs:
        if os.path.exists(os.path.join(d, filename)):
            return send_from_directory(d, filename)
    return send_from_directory(static_dirs[0], filename)

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
