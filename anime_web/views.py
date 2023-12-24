from flask import Blueprint

# defining this file as the blueprint of the application
# defined the blueprint
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return '<h1>Test</h1>'
