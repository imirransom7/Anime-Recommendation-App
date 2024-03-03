from . import db
from flask_login import UserMixin


class AnimeData(db.Model):
    anime_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50))
    score = db.Column(db.Text)
    genres = db.Column(db.Text)
    synopsis = db.Column(db.Text)
    type = db.Column(db.Text)
    episodes = db.Column(db.Integer)
    aired = db.Column(db.Text)
    studios = db.Column(db.String(50))
    duration = db.Column(db.Text)
    rating = db.Column(db.Text)
    rank = db.Column(db.Integer)
    image_url = db.Column(db.Text)
    favorites = db.Column(db.Integer)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


class AnimeDataset(db.Model):
    anime_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Strings(70))
    score = db.Column(db.Float)
    type = db.Column(db.Strings(20))
    # The columns where the anime is not finished show up as 'UNKNOWN'; might have to change to something else
    episodes = db.Column(db.Integer)
    aired = db.Strings(30)
    premiered = db.Strings(30)
    status = db.Strings(30)
    producers = db.Strings(100)
    licensors = db.Stringd(100)
    studios = db.Strings(100)
    source = db.Strings(20)
    duration = db.Strings(30)
    rating = db.Strings(40)
    rank = db.Integer()
    popularity = db.Integer()
    favorites = db.Integer()
    scored_by = db.Integer()
    members = db.Integer()
    images_url = db.Text()


class AnimeImages(db.Model):
    anime_id = db.Column(db.Integer, db.ForeignKey('anime_id'), nullable=False)
    images = db.Column(db.Text)


class AnimeGenres(db.Model):
    anime_id = db.Column(db.Integer, db.ForeignKey('anime_id'), nullable=False)
    name = db.Column(db.String(35))

    # This needs to go to the AnimeDataset Model when it is made
    genre = db.relationship('AnimeDataset', backref='anime')


# class AnimeFiltered(db.Model):
#     anime_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     score = db.Column(db.Text)
#     genres = db.Column(db.Text)
#     synopsis = db.Column(db.Text)
#     type = db.Column(db.Text)
#     episodes = db.Column(db.Integer)
#     aired = db.Column(db.Text)
#     studios = db.Column(db.String(50))
#     duration = db.Column(db.Text)
#     rating = db.Column(db.Text)
#     rank = db.Column(db.Integer)
#     image_url = db.Column(db.Text)
#     favorites = db.Column(db.Integer)


# class AnimeDataset(db.Model):
#     anime_id = db.Column(db.Integer, primary_key=True, unique=True)
#     name = db.Column(db.String(50))
#     score = db.Column(db.Float)
#     genre = db.Column(db.String(50))
#     english_name = db.Column(db.String(50))
#     japanese_name = db.Column(db.Text)
#     synopsis = db.Column(db.Text)
#     type = db.Column(db.Text)
#     episodes = db.Column(db.String(20))
#     aired = db.Column(db.Text)
#     premiered = db.Column(db.Text)
#     producers = db.Column(db.String(100))
#     licensors = db.Column(db.String(100))
#     studios = db.Column(db.String(50))
#     source = db.Column(db.Text)
#     duration = db.Column(db.Text)
#     rating = db.Column(db.Text)
#     ranked = db.Column(db.Text)
#     popularity = db.Column(db.Integer)
#     members = db.Column(db.Integer)
#     favorites = db.Column(db.Integer)
#     watching = db.Column(db.Integer)
#     completed = db.Column(db.Integer)
#     on_hold = db.Column(db.Integer)
#     dropped = db.Column(db.Integer)
