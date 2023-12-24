from . import db
from flask_login import UserMixin


class Anime(db.Model):
    anime_id = db.Column(db.Integer, primary_key=True)
    anime_img_id = db.Column(db.Integer)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
