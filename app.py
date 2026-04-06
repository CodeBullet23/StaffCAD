from flask import Flask
from extensions import db, login_manager
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'change-this-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cad.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from auth import auth_bp
    from actions import actions_bp
    from staff import staff_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(actions_bp, url_prefix='/actions')
    app.register_blueprint(staff_bp)
    
    with app.app_context():
        from models import User
        db.create_all()
        create_default_admin()

    return app

def create_default_admin():
    from models import User
    from werkzeug.security import generate_password_hash

    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            role='admin',
            must_change_password=True,
            password_hash=generate_password_hash('admin123')
        )
        db.session.add(admin)
        db.session.commit()


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
