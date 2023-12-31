from flask import Blueprint, render_template
import pandas as pd

anime_bp = Blueprint('anime', __name__)

# getting the more current anime since there is a lot of outdated anime
df1 = pd.read_csv('anime-dataset-2023.csv')
# making df into a dictionary to be able to use in the html templates
df_dict = dict(df1)

member_sort = df1.sort_values(by=['Members'], ascending=False).head(6000)

new_dict = dict(member_sort)
# list for the respective columns from member_sort
anime_name = list(member_sort['Name'])
image_list = list(member_sort['Image URL'])
anime_id = list(member_sort['anime_id'])
anime_synopsis = list(member_sort['Synopsis'])
anime_genre = list(member_sort['Genres'])
anime_score = list(member_sort['Score'])
anime_rating = list(member_sort['Rating'])
anime_type = list(member_sort['Type'])
anime_episodes = list(member_sort['Episodes'])
anime_aired = list(member_sort['Aired'])
anime_duration = list(member_sort['Duration'])
anime_studio = list(member_sort['Studios'])

score_sort = df1.sort_values(by=['Score'], ascending=False)
score_sort = score_sort.drop(score_sort[score_sort['Score'].str.contains('UNKNOWN')].index)
score_sort = score_sort.head(6000)
# list for respective columns for the highest rated order
score_name = list(score_sort['Name'])
score_id = list(score_sort['anime_id'])

# opening text file with urls to iterate over them
with open('anime_web/static/member_url_sort.txt', 'r') as file:
    image_urls = file.readlines()
anime_pics = image_urls

# same as above, but in order from the highest rated
with open('anime_web/static/score_img_sort.txt', 'r')as file:
    score_img_url = file.readlines()

# a range used to help get a list of both the names and the images of the anime
ranger = range(len(anime_id))
# Used for iterating the list of the keys
ranger1 = range(len(list(new_dict['anime_id'])))


# Turning string in the genres to list, so I can list them out on the web page
genre_anime = [gen.split(',') for gen in anime_genre]


@anime_bp.route('/anime')
def anime():
    # Check in the Flask console
    return render_template('anime.html', range=ranger, anime_name=anime_name,
                           anime_pics=anime_pics, anime_id=anime_id)


@anime_bp.route('/anime/<int:anime_index>')
def anime_details(anime_index):
    name_anime = anime_name[anime_index]
    pics_anime = anime_pics[anime_index]
    summary = anime_synopsis[anime_index]
    genre = genre_anime[anime_index]
    score = anime_score[anime_index]
    rating = anime_rating[anime_index]
    type_anime = anime_type[anime_index]
    episodes = anime_episodes[anime_index]
    aired = anime_aired[anime_index]
    duration = anime_duration[anime_index]
    studio = anime_studio[anime_index]

    # Redner the details page with the fetched data
    return render_template('anime_details.html', name_anime=name_anime,
                           pics_anime=pics_anime, anime_index=anime_index, new_dict=new_dict,
                           summary=summary, genre=genre, range=ranger,
                           score=score, rating=rating, type_anime=type_anime,
                           episodes=episodes, aired=aired, duration=duration,
                           studio=studio)


@anime_bp.route('/anime/highest-rated')
def highest_score():

    return render_template('highest_rated.html', range=ranger, score_name=score_name,
                           anime_pics=score_img_url, anime_id=anime_id)
