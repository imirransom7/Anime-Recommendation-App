# commands.py
from flask import Blueprint
from flask.cli import with_appcontext
from .models import db, AnimeFiltered
import pandas as pd


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
    df = pd.read_csv('anime-dataset-2023.csv')

    grouped = df.groupby(['anime_id', 'Name', 'Score',
                          'Genres', 'Synopsis', 'Type',
                          'Episodes', 'Aired', 'Studios',
                          'Rating', 'Rank', 'Image URL']).Favorites.size()

    with db.session.begin(subtransactions=True):
        for name, group in grouped:
            anime_instance = AnimeFiltered(
                anime_id=name[0],
                name=name[1],
                score=name[2],
                genres=name[3],
                synopsis=name[4],
                type=name[5],
                episodes=name[6],
                aired=name[7],
                studios=name[8],
                duration=name[9],
                rating=name[10],
                rank=name[11],
                image_url=name[12],
                favorites=group['Favorites'].size,
            )
            db.session.add(anime_instance)

    # Commit the changes to the database
    db.session.commit()
