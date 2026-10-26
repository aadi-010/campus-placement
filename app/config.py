import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Detect serverless environment (e.g. Vercel, AWS Lambda)
IS_SERVERLESS = bool(os.environ.get('VERCEL') or os.environ.get('AWS_LAMBDA_FUNCTION_NAME'))

if IS_SERVERLESS:
    INSTANCE_DIR = '/tmp'
else:
    INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
    try:
        os.makedirs(INSTANCE_DIR, exist_ok=True)
    except OSError:
        INSTANCE_DIR = '/tmp'

def get_database_uri():
    raw_url = os.environ.get('DATABASE_URL')
    if raw_url:
        # Convert deprecated postgres:// to postgresql:// for SQLAlchemy
        if raw_url.startswith('postgres://'):
            raw_url = raw_url.replace('postgres://', 'postgresql://', 1)
        return raw_url
    db_path = os.path.join(INSTANCE_DIR, 'campusprep.db')
    return f"sqlite:///{db_path}"

class Config:
    """Base application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'campusprep-hackathon-insecure-dev-secret-key-2026')
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = 3600

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'true').lower() == 'true'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    SESSION_COOKIE_SECURE = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
