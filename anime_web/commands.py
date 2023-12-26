from flask import Blueprint, render_template
from flask.cli import with_appcontext
from .models import db, AnimeData
import pandas as pd


db_commands = Blueprint("db_commands", __name__)

# getting the more current anime since there is a lot of outdated anime
df1 = pd.read_csv('anime-dataset-2023.csv')
member_sort = df1.sort_values(by=['Members'], ascending=False).head(6000)

# Made a list for anime names and the url image links
anime_name = list(member_sort['Name'])
image_list = list(member_sort['Image URL'])
# combine both the list so the names iterates next to the images
anime_list = zip(anime_name, image_list)

anime_dict = dict(df1)
name_list = list(anime_dict['Name'])


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


# opening text file with urls to iterate over them
with open('anime_web/static/member_url_sort.txt', 'r') as file:
    image_urls = file.readlines()

anime_images = [
    {
        'Name': index,
        'image_url': url,
    }
    for index, url in enumerate(image_urls)
]

anime_img_list = zip(name_list, anime_images)
new_line = '\n'


@db_commands.route('/anime')
def anime():
    anime_data = AnimeData.query.all()
    # Check in the Flask console
    return render_template('anime.html', anime_img_list=anime_img_list, anime_images=anime_images,
                           name_list=name_list, new_line=new_line)  # anime_dict=anime_dict,
