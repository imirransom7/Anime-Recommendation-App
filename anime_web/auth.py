from flask import Blueprint

# defining this file as the blueprint of the application
# defined the blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return '<p>Login</p>'


@auth.route('/logout')
def logout():
    return '<p>Logout</p>'


@auth.route('/sign-up')
def sin_up():
    return '<p>Sign Up</p>'

