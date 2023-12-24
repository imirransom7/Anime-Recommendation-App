from flask import Flask


# How to initialize Flask
def create_app():
    app = Flask(__name__)
    # Secure the cookies session data; the secret key for the app
    app.config["SECRET_KEY"] = 'THIS IS THE SECRET KEY'


    # importing the blueprints
    from .views import views
    from .auth import auth

    # registering the blueprints; accessing all urls with a /
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
