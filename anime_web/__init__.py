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
    from .csv_importer import import_csv_to_anime_dataset
    # importing the blueprints
    from .views import views
    from .auth import auth

    # registering the blueprints; accessing all urls with a /
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # to load file to run it before it initializes or create the databases
    from .models import User

    with app.app_context():
        db.create_all()
        # Import data from CSV to AnimeDataset
        csv_file_path = 'anime-filtered.csv'  # Update with your CSV file path
        import_csv_to_anime_dataset(csv_file_path)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('anime_web/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database~')
