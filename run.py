import os
from app import create_app
from app.extensions import db

env = os.environ.get('FLASK_ENV', 'development')
app = create_app(env)

with app.app_context():
    # Ensure database tables exist
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = env == 'development'
    print(f" * Starting CampusPrep on http://127.0.0.1:{port} (env: {env})")
    app.run(host='0.0.0.0', port=port, debug=debug)
