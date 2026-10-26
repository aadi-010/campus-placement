from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        college = request.form.get('college', '').strip()
        graduation_year = request.form.get('graduation_year')
        target_role = request.form.get('target_role', '').strip()

        # Validation
        if not full_name or not email or not password:
            flash('Full name, email, and password are required.', 'danger')
            return render_template('auth/register.html', full_name=full_name, email=email)

        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'danger')
            return render_template('auth/register.html', full_name=full_name, email=email)

        if password != confirm_password:
            flash('Passwords do not match. Please verify.', 'danger')
            return render_template('auth/register.html', full_name=full_name, email=email)

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('An account with this email already exists. Please log in.', 'warning')
            return redirect(url_for('auth.login'))

        # Create new user
        user = User(
            full_name=full_name,
            email=email,
            college=college or None,
            graduation_year=int(graduation_year) if graduation_year and graduation_year.isdigit() else None,
            target_role=target_role or 'Software Engineer'
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash('Account created successfully! Welcome to CampusPrep.', 'success')
        return redirect(url_for('dashboard.index'))

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated and request.method == 'GET' and not request.args.get('switch'):
        flash(f'You are already logged in as {current_user.email}.', 'info')
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        if current_user.is_authenticated:
            logout_user()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        remember = bool(request.form.get('remember'))

        if not email or not password:
            flash('Please enter both email and password.', 'danger')
            return render_template('auth/login.html', email=email)

        user = User.query.filter_by(email=email).first()
        if not user:
            # Auto-register new students on first login attempt if password is valid
            if len(password) >= 6:
                display_name = email.split('@')[0].replace('.', ' ').replace('_', ' ').title()
                user = User(
                    full_name=display_name,
                    email=email,
                    target_role='Software Engineer'
                )
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=remember)
                flash(f'Account created successfully! Welcome to CampusPrep, {user.full_name}.', 'success')

                next_page = request.args.get('next')
                if next_page and next_page.startswith('/'):
                    if '?__path=' in next_page:
                        next_page = next_page.split('?__path=')[0]
                    return redirect(next_page)
                return redirect(url_for('dashboard.index'))
            else:
                flash('No account found for this email. Password must be at least 6 characters to register.', 'danger')
                return render_template('auth/login.html', email=email)

        if not user.check_password(password):
            flash('Incorrect password for this account. Please verify or use the One-Click Demo Student Login below.', 'danger')
            return render_template('auth/login.html', email=email)

        login_user(user, remember=remember)
        flash(f'Welcome back, {user.full_name}!', 'success')
        
        next_page = request.args.get('next')
        if next_page and next_page.startswith('/'):
            if '?__path=' in next_page:
                next_page = next_page.split('?__path=')[0]
            return redirect(next_page)
        return redirect(url_for('dashboard.index'))

    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out safely.', 'info')
    return redirect(url_for('main.index'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'update_profile':
            full_name = request.form.get('full_name', '').strip()
            college = request.form.get('college', '').strip()
            graduation_year = request.form.get('graduation_year')
            target_role = request.form.get('target_role', '').strip()
            daily_goal = request.form.get('daily_goal')

            if full_name:
                current_user.full_name = full_name
            current_user.college = college or None
            if graduation_year and graduation_year.isdigit():
                current_user.graduation_year = int(graduation_year)
            current_user.target_role = target_role or 'Software Engineer'
            if daily_goal and daily_goal.isdigit():
                current_user.daily_goal = max(1, int(daily_goal))

            db.session.commit()
            flash('Profile details updated successfully.', 'success')

        elif action == 'change_password':
            current_pwd = request.form.get('current_password', '')
            new_pwd = request.form.get('new_password', '')
            confirm_pwd = request.form.get('confirm_new_password', '')

            if not current_user.check_password(current_pwd):
                flash('Current password is incorrect.', 'danger')
            elif len(new_pwd) < 6:
                flash('New password must be at least 6 characters.', 'danger')
            elif new_pwd != confirm_pwd:
                flash('New passwords do not match.', 'danger')
            else:
                current_user.set_password(new_pwd)
                db.session.commit()
                flash('Password changed successfully!', 'success')

        return redirect(url_for('auth.profile'))

    return render_template('dashboard/profile.html')
