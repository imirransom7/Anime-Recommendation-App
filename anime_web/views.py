from flask import Blueprint
from flask import render_template

# defining this file as the blueprint of the application
# defined the blueprint
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')
