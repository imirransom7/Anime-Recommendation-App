from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
# Import the function from models

db = SQLAlchemy()
DB_NAME = 'database.db'


# How to initialize Flask
def create_app():
    app = Flask(__name__)
    # Secure the cookies session data; the secret key for the app
    app.config["SECRET_KEY"] = 'THIS IS THE SECRET KEY'
    # Storing the database inside the anime_web folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #  taking the database and telling it this the app we are going to use
    db.init_app(app)
    # importing the blueprints
    from .views import views
    from .auth import auth
    # from .commands import db_commands
    from .anime import anime_bp
    # registering the blueprints; accessing all urls with a /
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # app.register_blueprint(db_commands)
    app.register_blueprint(anime_bp)
    # to load file to run it before it initializes or create the databases
    from .models import User, AnimeData

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(int(_id))

    return app


def create_database(app):
    if not path.exists('anime_web/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database~')
