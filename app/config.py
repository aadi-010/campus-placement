import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Auto-load .env file if present (zero-dependency fallback)
def _load_dotenv_if_present():
    env_file = os.path.join(BASE_DIR, '.env')
    if os.path.isfile(env_file):
        try:
            with open(env_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#') or '=' not in line:
                        continue
                    k, v = line.split('=', 1)
                    k = k.strip()
                    v = v.strip().strip("'\"")
                    if k not in os.environ:
                        os.environ[k] = v
        except Exception:
            pass

_load_dotenv_if_present()

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
    
    supa_url = os.environ.get('SUPABASE_URL', 'https://tcnktohuqrjzipnfnafw.supabase.co')
    if not raw_url and 'tcnktohuqrjzipnfnafw' in supa_url:
        raw_url = 'postgresql+psycopg://campusprep_admin.tcnktohuqrjzipnfnafw:CampusPrep_2026_SecurePass!@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres?sslmode=require'

    if raw_url:
        # Convert legacy postgres:// to postgresql://
        if raw_url.startswith('postgres://'):
            raw_url = raw_url.replace('postgres://', 'postgresql://', 1)
        
        # When raw postgresql:// is provided without explicit driver, select best installed driver
        if raw_url.startswith('postgresql://'):
            try:
                import psycopg
                raw_url = raw_url.replace('postgresql://', 'postgresql+psycopg://', 1)
            except ImportError:
                try:
                    import pg8000
                    raw_url = raw_url.replace('postgresql://', 'postgresql+pg8000://', 1)
                except ImportError:
                    pass
        return raw_url

    db_path = os.path.join(INSTANCE_DIR, 'campusprep.db')
    return f"sqlite:///{db_path}"

class Config:
    """Base application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'campusprep-production-saas-security-key-2026')
    
    # Database
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }
    
    # Supabase Integration
    SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://tcnktohuqrjzipnfnafw.supabase.co')
    SUPABASE_PUBLISHABLE_KEY = os.environ.get('SUPABASE_PUBLISHABLE_KEY', 'sb_publishable_wSMMzkt_ado0gXqYPJW6RA_8Uj1FwUb')
    SUPABASE_SECRET_KEY = os.environ.get('SUPABASE_SECRET_KEY')
    SUPABASE_JWKS_URL = os.environ.get('SUPABASE_JWKS_URL', 'https://tcnktohuqrjzipnfnafw.supabase.co/auth/v1/.well-known/jwks.json')

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
    SQLALCHEMY_ENGINE_OPTIONS = {}

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
