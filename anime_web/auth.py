from flask import Blueprint
from flask import render_template
# defining this file as the blueprint of the application
# defined the blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html', text="testing")


@auth.route('/logout')
def logout():
    return '<p>Logout</p>'


@auth.route('/sign-up')
def sin_up():
    return render_template('sign_up.html')

