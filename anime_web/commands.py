from flask import Blueprint, render_template
from flask.cli import with_appcontext
from .models import db, AnimeData
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


@db_commands.route('/anime')
def anime():
    anime_data = AnimeData.query.all()


