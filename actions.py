from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from extensions import db
from models import Action

actions_bp = Blueprint('actions', __name__)


@actions_bp.route('/')
@login_required
def dashboard():
    actions = Action.query.order_by(Action.created_at.desc()).limit(50).all()
    return render_template('dashboard.html', actions=actions)


@actions_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_action():
    if request.method == 'POST':
        target_user = request.form.get('target_user', '').strip()
        platform = request.form.get('platform', '').strip()
        action_type = request.form.get('action_type', '').strip()
        reason = request.form.get('reason', '').strip()

        if not target_user or not platform or not action_type or not reason:
            flash('All fields are required', 'danger')
            return redirect(url_for('actions.new_action'))

        action = Action(
            staff_id=current_user.id,
            target_user=target_user,
            platform=platform,
            action_type=action_type,
            reason=reason
        )
        db.session.add(action)
        db.session.commit()
        flash('Action logged', 'success')
        return redirect(url_for('actions.dashboard'))

    return render_template('action_new.html')
