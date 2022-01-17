from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
# DB_NAME = "database.db" # Use for sqllite
DB_NAME = "twitterjobdb" # postgresql DB name


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iMORPHr Key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database///{DB_NAME}' # Connection sting for sqllite

     # Change Connection sting as per you machine
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:123mrp.NET@localhost/{DB_NAME}'
    db.init_app(app)

    from .views.dashboard import dashboard_bluprint
    from .views.auth import auth

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(dashboard_bluprint, url_prefix='/')

    # from .models.models import User, Note

    from .models.user_model import User
    from .models.note_model import Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('app/database/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')