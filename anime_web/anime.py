from flask import Blueprint, render_template
import pandas as pd

anime = Blueprint('anime', __name__)

# getting the more current anime since there is a lot of outdated anime
df1 = pd.read_csv('anime-dataset-2023.csv')
member_sort = df1.sort_values(by=['Members'], ascending=False).head(6000)

new_dict = dict(df1)
# Made a list for anime names and the url image links
anime_name = list(member_sort['Name'])
image_list = list(member_sort['Image URL'])
anime_id = list(member_sort['anime_id'])
# combine both the list so the names iterates next to the images
anime_list = zip(anime_name, image_list)
anime_synopsis = list(member_sort['Synopsis'])
anime_genre = list(member_sort['Genres'])
# anime_dict = dict(df1)
# name_list = list(anime_dict['Name'])

