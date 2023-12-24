from . import db
from flask_login import UserMixin


class Anime(db.Model):
    anime_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    score = db.Column(db.Decimal(1, 2))
    genre = db.Column(db.String(50))
    english_name = db.Column(db.String(50))
    japanese_name = db.Column(db.Text)
    synopsis = db.Column(db.Text)
    type = db.Column(db.Text)
    episodes = db.Column(db.Integer)
    aired = db.Column(db.Text)
    premiered = db.Column(db.Text)
    producers = db.Column(db.String(100))
    licensors = db.Column(db.String(100))
    studios = db.Column(db.String(50))
    source = db.Column(db.Text)
    duration = db.Column(db.Text)
    rating = db.Column(db.Text)
    ranked = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    members = db.Column(db.Integer)
    favorites = db.Column(db.Integer)
    watching = db.Column(db.Integer)
    completed = db.Column(db.Integer)
    on_hold = db.Column(db.Integer)
    dropped = db.Column(db.Integer)









class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
