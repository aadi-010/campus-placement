from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from app.extensions import db
from app.models.company import CompanyTrack, CompanyChecklist

companies_bp = Blueprint('companies', __name__)

@companies_bp.route('/')
@login_required
def index():
    companies = CompanyTrack.query.order_by(CompanyTrack.name).all()
    
    # Calculate completion percentage for each company for current user
    user_checklists = CompanyChecklist.query.filter_by(user_id=current_user.id).all()
    user_done_map = {}
    for item in user_checklists:
        if item.is_completed:
            user_done_map.setdefault(item.company_id, set()).add(item.item_index)

    progress_map = {}
    for c in companies:
        total_items = len(c.checklist_items)
        done_count = len(user_done_map.get(c.id, set()))
        pct = int((done_count / total_items) * 100) if total_items > 0 else 0
        progress_map[c.id] = {'done': done_count, 'total': total_items, 'percentage': pct}

    return render_template('companies/index.html',
        companies=companies,
        progress_map=progress_map
    )

@companies_bp.route('/<slug>')
@login_required
def detail(slug):
    company = CompanyTrack.query.filter_by(slug=slug).first_or_404()

    # User checklist state
    checklists = CompanyChecklist.query.filter_by(
        user_id=current_user.id, company_id=company.id
    ).all()
    completed_indices = set(c.item_index for c in checklists if c.is_completed)

    return render_template('companies/detail.html',
        company=company,
        completed_indices=completed_indices
    )

@companies_bp.route('/api/<int:company_id>/checklist', methods=['POST'])
@login_required
def toggle_checklist_api(company_id):
    data = request.get_json() or {}
    item_index = data.get('item_index')

    if item_index is None:
        return jsonify({'success': False, 'error': 'Missing item_index'}), 400

    item = CompanyChecklist.query.filter_by(
        user_id=current_user.id, company_id=company_id, item_index=int(item_index)
    ).first()

    if item:
        item.is_completed = not item.is_completed
    else:
        item = CompanyChecklist(
            user_id=current_user.id,
            company_id=company_id,
            item_index=int(item_index),
            is_completed=True
        )
        db.session.add(item)

    db.session.commit()
    return jsonify({'success': True, 'is_completed': item.is_completed})
