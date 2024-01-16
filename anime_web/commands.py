from flask import Blueprint, render_template
from flask.cli import with_appcontext
from .models import db, AnimeData
import pandas as pd
from sqlalchemy import desc, not_

db_commands = Blueprint("db_commands", __name__)


@db_commands.cli.command("init-db")
@with_appcontext
def init_db():
    # Create the database tables
    db.create_all()


@db_commands.cli.command("import-data")
@with_appcontext
def import_data():
    # Load data into the AnimeDataset table
    # Add your data import logic here
    df = pd.read_csv('anime_web/anime-dataset-2023.csv')

    group = df.groupby(['anime_id', 'Name', 'Score',
                        'Genres', 'Synopsis', 'Type',
                        'Episodes', 'Aired', 'Studios',
                        'Duration', 'Rating', 'Rank',
                        'Image URL']).Favorites.size().reset_index()
    print(f"Number of rows before import: {len(df)}")
    grouped = pd.DataFrame(group)
    with db.session.begin():
        for index, row in grouped.iterrows():
            anime_instance = AnimeData(
                anime_id=row['anime_id'],
                name=row['Name'],
                score=row['Score'],
                genres=row['Genres'],
                synopsis=row['Synopsis'],
                type=row['Type'],
                episodes=row['Episodes'],
                aired=row['Aired'],
                studios=row['Studios'],
                duration=row['Duration'],  # Assuming Duration is a column in your CSV
                rating=row['Rating'],
                rank=row['Rank'],
                image_url=row['Image URL'],
                favorites=row['Favorites'],
            )
            db.session.add(anime_instance)

    # Commit the changes to the database
    db.session.commit()
    print(f"Number of rows after import: {AnimeData.query.count()}")


@db_commands.route('/anime-command')
def anime():
    anime_data = AnimeData.query.all()
    return render_template('anime_command.html', anime_data=anime_data)


with open('anime_web/static/score_img_sort.txt', 'r')as file:
    score_img_url = file.readlines()

ranger = range(len(score_img_url))

with open('anime_web/static/image_urls.txt') as file:
    all_images = file.readlines()


@db_commands.route('/anime-home')
def anime_home():
    anime_list = AnimeData.query.all()
    return render_template("anime_home.html", anime_list=anime_list,
                           images=all_images, range=ranger)


@db_commands.route('/anime-highest-rated')
def anime_rated():
    #  Query the AnimeData table, filter out rows with "UNKNOWN" values, and sort by score in descending order
    rated_anime = AnimeData.query.filter(not_(AnimeData.score == 'UNKNOWN')).order_by(desc(AnimeData.score)).all()
    return render_template('rated_anime.html', rated_anime=rated_anime,
                           images=score_img_url, range=ranger)


@db_commands.route('/anime-home/<int:anime_id>')
def anime_info(anime_id):
    anime_data = AnimeData.query.get(anime_id)

    return render_template('anime_info.html', anime_data=anime_data)


@db_commands.route('/anime-most-popular')
def most_popular():
    return render_template('most_popular.html')
