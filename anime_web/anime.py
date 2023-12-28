from flask import Blueprint, render_template
import pandas as pd

anime_bp = Blueprint('anime', __name__)

# getting the more current anime since there is a lot of outdated anime
df1 = pd.read_csv('anime-dataset-2023.csv')
# making df into a dictionary to be able to use in the html templates
df_dict = dict(df1)

member_sort = df1.sort_values(by=['Members'], ascending=False).head(6000)

new_dict = dict(df1)
# Made list for the respective columns
anime_name = list(member_sort['Name'])
image_list = list(member_sort['Image URL'])
anime_id = list(member_sort['anime_id'])
anime_synopsis = list(member_sort['Synopsis'])
anime_genre = list(member_sort['Genres'])


# opening text file with urls to iterate over them
with open('anime_web/static/member_url_sort.txt', 'r') as file:
    image_urls = file.readlines()
anime_pics = image_urls
anime_images = [
    {
        'Name': index,
        'image_url': url,
    }
    for index, url in enumerate(image_urls)
]
# a range used to help get a list of both the names and the images of the anime
ranger = range(len(anime_images))


@anime_bp.route('/anime')
def anime():
    # Check in the Flask console
    return render_template('anime.html', ranger=ranger, anime_name=anime_name,
                           anime_pics=anime_pics, anime_id=anime_id)


# Turning string in the genres to list, so I can list them out on the web page
genre_anime = []
for gen in anime_genre:
    genre_anime.append(gen.split(','))


@anime_bp.route('/anime/<int:anime_index>')
def anime_details(anime_index):
    name_anime = anime_name[anime_index]
    pics_anime = anime_pics[anime_index]
    summary = anime_synopsis[anime_index]
    genre = genre_anime[anime_index]

    # Redner the details page with the fetched data
    return render_template('anime_details.html', name_anime=name_anime,
                           pics_anime=pics_anime, anime_index=anime_index, new_dict=new_dict,
                           summary=summary, genre=genre, ranger=ranger)
