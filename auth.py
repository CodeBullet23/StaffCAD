from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from extensions import db
from models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash('Invalid credentials', 'danger')
            return redirect(url_for('auth.login'))

        login_user(user)
        if user.must_change_password:
            return redirect(url_for('auth.change_password'))

        return redirect(url_for('actions.dashboard'))

    return render_template('login.html')


@auth_bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        new_password = request.form.get('new_password', '')
        confirm = request.form.get('confirm_password', '')

        if not new_password:
            flash('Password cannot be empty', 'danger')
            return redirect(url_for('auth.change_password'))

        if new_password != confirm:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('auth.change_password'))

        current_user.password_hash = generate_password_hash(new_password)
        current_user.must_change_password = False
        db.session.commit()
        flash('Password updated', 'success')
        return redirect(url_for('actions.dashboard'))

    return render_template('change_password.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
