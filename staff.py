from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from extensions import db
from models import User

staff_bp = Blueprint('staff', __name__)


def admin_required(func):
    def wrapper(*args, **kwargs):
        if current_user.role != 'admin':
            flash("You do not have permission to access this page.", "danger")
            return redirect(url_for('actions.dashboard'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


@staff_bp.route('/staff')
@login_required
@admin_required
def staff_list():
    users = User.query.all()
    return render_template('staff_list.html', users=users)


@staff_bp.route('/staff/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_staff():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        role = request.form.get('role')

        if not username or not password:
            flash("All fields are required.", "danger")
            return redirect(url_for('staff.add_staff'))

        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "danger")
            return redirect(url_for('staff.add_staff'))

        new_user = User(
            username=username,
            password_hash=generate_password_hash(password),
            role=role,
            must_change_password=True
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Staff member added successfully!", "success")
        return redirect(url_for('staff.staff_list'))

    return render_template('staff_add.html')
