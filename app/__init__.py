import os
from flask import Flask, render_template
from app.config import config_by_name
from app.extensions import db, login_manager, csrf

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name, config_by_name['default']))

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Register Blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.aptitude import aptitude_bp
    from app.routes.coding import coding_bp
    from app.routes.interviews import interviews_bp
    from app.routes.mock_tests import mock_tests_bp
    from app.routes.companies import companies_bp
    from app.routes.resources import resources_bp
    from app.routes.progress import progress_bp
    from app.routes.api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(aptitude_bp, url_prefix='/aptitude')
    app.register_blueprint(coding_bp, url_prefix='/coding')
    app.register_blueprint(interviews_bp, url_prefix='/interview')
    app.register_blueprint(mock_tests_bp, url_prefix='/mock-tests')
    app.register_blueprint(companies_bp, url_prefix='/companies')
    app.register_blueprint(resources_bp, url_prefix='/resources')
    app.register_blueprint(progress_bp, url_prefix='/progress')
    app.register_blueprint(api_bp, url_prefix='/api')

    # Exclude API endpoints from CSRF if using Fetch/JSON headers with X-CSRFToken
    # Note: Flask-WTF CSRFProtect checks request header 'X-CSRFToken' automatically!

    # Global context processors and Jinja globals
    app.jinja_env.globals.update(
        int=int,
        round=round,
        max=max,
        min=min,
        len=len,
        str=str
    )

    @app.context_processor
    def inject_global_vars():
        from datetime import datetime
        now = datetime.now()
        greeting = "Good evening" if now.hour >= 17 else ("Good afternoon" if now.hour >= 12 else "Good morning")
        return {
            'current_year': now.year,
            'time_greeting': greeting,
            'app_name': 'CampusPrep',
            'app_tagline': 'Prepare Smarter. Practice Better. Get Placed.'
        }

    # Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    return app
