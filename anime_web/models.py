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
    name = db.Column(db.String(70))
    score = db.Column(db.Float)
    type = db.Column(db.String(20))
    # The columns where the anime is not finished show up as 'UNKNOWN'; might have to change to something else
    episodes = db.Column(db.Integer)
    aired = db.Column(db.String(30))
    premiered = db.Column(db.String(20))
    status = db.Column(db.String(20))
    producers = db.Column(db.String(100))
    licensors = db.Column(db.String(100))
    studios = db.Column(db.String(100))
    source = db.Column(db.String(20))
    duration = db.Column(db.String(30))
    rating = db.Column(db.String(40))
    rank = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    favorites = db.Column(db.Integer)
    scored_by = db.Column(db.Integer)
    members = db.Column(db.Integer)
    images_url = db.Column(db.Text)
    genre = db.relationship('AnimeDataset', backref='anime_dataset')
    images = db.relationship('AnimeDataset', backref='anime_dataset')


class AnimeImages(db.Model):
    anime_id = db.Column(db.Integer, db.ForeignKey('anime_id'), nullable=False)
    images = db.Column(db.Text)


class AnimeGenres(db.Model):
    anime_id = db.Column(db.Integer, db.ForeignKey('anime_dataset.anime_id'), nullable=False)
    name = db.Column(db.String(35))

    # This needs to go to the AnimeDataset Model when it is made
    # genre = db.relationship('AnimeDataset', backref='anime')


class UserDetails(db.model):
    # id for the users from the anime dataset (not the anime dataset mmodel)
    mal_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Strings(100))
    gender = db.Column(db.Strings(20))
    birthday = db.Column(db.Date)
    location = db.Column(db.Text)
    joined = db.Column(db.Text)
    days_watched = db.Column(db.Integer)
    mean_score = db.Column(db.Float)
    watching = db.Column(db.Integer)
    completed = db.Column(db.Integer)
    on_hold = db.Column(db.Integer)
    dropped = db.Column(db.Integer)
    plan_to_watch = db.Column(db.Integer)
    total_entries = db.Column(db.Integer)
    rewatched = db.Column(db.Integer)
    episodes_watched = db.Column(db.Integer)
    age = db.Column(db.Integer)



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
