from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models.aptitude import Bookmark, AptitudeQuestion, AptitudeAttempt
from app.models.coding import CodingChallenge, CodingSubmission
from app.models.interview import InterviewQuestion, InterviewProgress
from app.models.mock_test import MockTestAttempt
from app.services.readiness import calculate_readiness_score

api_bp = Blueprint('api', __name__)

@api_bp.route('/bookmark/toggle', methods=['POST'])
@login_required
def toggle_bookmark():
    """Toggle a bookmark for an aptitude question, interview question, coding challenge, or resource"""
    data = request.get_json() or {}
    item_type = data.get('item_type')
    item_id = data.get('item_id')

    if not item_type or not item_id:
        return jsonify({'success': False, 'error': 'Missing item_type or item_id'}), 400

    existing = Bookmark.query.filter_by(
        user_id=current_user.id,
        item_type=str(item_type),
        item_id=int(item_id)
    ).first()

    if existing:
        db.session.delete(existing)
        db.session.commit()
        return jsonify({'success': True, 'bookmarked': False, 'message': 'Bookmark removed'})
    else:
        new_bm = Bookmark(
            user_id=current_user.id,
            item_type=str(item_type),
            item_id=int(item_id)
        )
        db.session.add(new_bm)
        db.session.commit()
        return jsonify({'success': True, 'bookmarked': True, 'message': 'Bookmarked successfully'})

@api_bp.route('/dashboard', methods=['GET'])
@login_required
def api_dashboard():
    """Live dashboard stats snapshot in JSON format"""
    readiness = calculate_readiness_score(current_user.id)
    
    aptitude_count = AptitudeAttempt.query.filter_by(user_id=current_user.id).count()
    coding_count = db.session.query(CodingSubmission.challenge_id).filter_by(
        user_id=current_user.id, status='Accepted'
    ).distinct().count()
    interview_count = InterviewProgress.query.filter_by(
        user_id=current_user.id, is_reviewed=True
    ).count()

    mock_attempts = MockTestAttempt.query.filter_by(
        user_id=current_user.id, status='completed'
    ).all()
    avg_mock_score = (
        round(sum(m.score for m in mock_attempts if m.score is not None) / len(mock_attempts), 1)
        if mock_attempts else 0.0
    )

    return jsonify({
        'success': True,
        'user': {
            'id': current_user.id,
            'full_name': current_user.full_name,
            'email': current_user.email,
            'streak': current_user.current_streak
        },
        'stats': {
            'aptitude_attempted': aptitude_count,
            'coding_solved': coding_count,
            'interview_reviewed': interview_count,
            'avg_mock_score': avg_mock_score,
            'readiness_score': readiness['score']
        },
        'readiness': readiness
    })

@api_bp.route('/profile', methods=['GET', 'PATCH'])
@login_required
def api_profile():
    if request.method == 'GET':
        return jsonify({
            'success': True,
            'user': current_user.to_dict()
        })
    
    data = request.get_json() or {}
    if 'full_name' in data and data['full_name'].strip():
        current_user.full_name = data['full_name'].strip()
    if 'college' in data:
        current_user.college = data['college'].strip()
    if 'graduation_year' in data:
        try:
            current_user.graduation_year = int(data['graduation_year'])
        except (ValueError, TypeError):
            pass
    if 'target_role' in data:
        current_user.target_role = data['target_role'].strip()

    db.session.commit()
    return jsonify({
        'success': True,
        'message': 'Profile updated successfully',
        'user': current_user.to_dict()
    })

@api_bp.route('/supabase/config', methods=['GET'])
def supabase_public_config():
    """Return public Supabase configuration for client-side JavaScript SDK"""
    from app.services.supabase_service import supabase_service
    return jsonify({
        'success': True,
        'config': supabase_service.get_public_config()
    })

@api_bp.route('/supabase/status', methods=['GET'])
def supabase_status():
    """Check connectivity to Supabase Cloud Auth, JWKS, and live PostgreSQL database"""
    from app.services.supabase_service import supabase_service
    from sqlalchemy import text

    health = supabase_service.check_health()
    
    # Check PostgreSQL database status via SQLAlchemy
    db_status = 'disconnected'
    db_info = {}
    try:
        res = db.session.execute(text("SELECT current_database(), current_user, version()")).fetchone()
        if res:
            db_status = 'connected'
            db_info = {
                'database': res[0],
                'user': res[1],
                'dialect': db.engine.dialect.name
            }
    except Exception as e:
        db_status = f"error: {str(e)}"

    return jsonify({
        'success': True,
        'supabase': health,
        'database': {
            'status': db_status,
            'info': db_info
        }
    })

