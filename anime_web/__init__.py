from flask import Flask


# How to initialize Flask
def create_app():
    app = Flask(__name__)
    # Secure the cookies session data; the secret key for the app
    app.config["SECRET_KEY"] = 'THIS IS THE SECRET KEY'

    return app
