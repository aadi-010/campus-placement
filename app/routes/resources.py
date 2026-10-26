from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models.resource import PlacementResource
from app.models.aptitude import Bookmark

resources_bp = Blueprint('resources', __name__)

@resources_bp.route('/')
@login_required
def index():
    category = request.args.get('category', '').strip()
    search = request.args.get('q', '').strip()

    query = PlacementResource.query

    if category and category != 'all':
        query = query.filter_by(category=category)

    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (PlacementResource.title.ilike(search_filter)) |
            (PlacementResource.description.ilike(search_filter))
        )

    resources = query.order_by(PlacementResource.is_featured.desc(), PlacementResource.title).all()

    # Get distinct categories for filtering
    categories_raw = db.session.query(PlacementResource.category).distinct().all()
    categories = sorted([c[0] for c in categories_raw if c[0]])

    # Get user bookmarks for resources
    bookmarks = Bookmark.query.filter_by(user_id=current_user.id, item_type='resource').all()
    bookmarked_ids = set(b.item_id for b in bookmarks)

    return render_template('resources/index.html',
        resources=resources,
        categories=categories,
        selected_category=category,
        search_query=search,
        bookmarked_ids=bookmarked_ids
    )

@resources_bp.route('/api/list')
@login_required
def api_list():
    category = request.args.get('category', '').strip()
    search = request.args.get('q', '').strip()

    query = PlacementResource.query

    if category and category != 'all':
        query = query.filter_by(category=category)

    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (PlacementResource.title.ilike(search_filter)) |
            (PlacementResource.description.ilike(search_filter))
        )

    resources = query.order_by(PlacementResource.is_featured.desc(), PlacementResource.title).all()
    return jsonify({
        'success': True,
        'resources': [r.to_dict() for r in resources]
    })
