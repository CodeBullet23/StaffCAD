from datetime import datetime
from flask_login import UserMixin
from extensions import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(32), default='moderator')
    must_change_password = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    target_user = db.Column(db.String(128), nullable=False)
    platform = db.Column(db.String(32), nullable=False)  # 'discord', 'roblox', 'fivem'
    action_type = db.Column(db.String(32), nullable=False)  # 'warn', 'ban', 'kick', 'note'
    reason = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    staff = db.relationship('User', backref='actions')
