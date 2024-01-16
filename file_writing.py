import pandas as pd

df = pd.read_csv('anime-dataset-2023.csv')
# Taking out any anime that contains 'Hentai' as a genre
df = df.drop(df[df['Genres'].str.contains('Hentai')].index)

member_sort = df.sort_values(by=['Members'], ascending=False)
score_sort = df.sort_values(by=['Score'], ascending=False)
# Dropping all rows with UNKNOWN as a value since it is messing up the order of the list
score_sort = score_sort.drop(score_sort[score_sort['Score'].str.contains('UNKNOWN')].index)

score_url = 'score_img_sort.txt'

all_images_urls = 'all_images_urls.txt'
all_images = df['Image URL']

# writing list of image urls into a file
with open(score_url, 'w') as file:
    for url in all_images:
        # writes the urls one by one as it is iterated through the list
        file.write(url + "\n")

print(f'Image Urls have beem written to {all_images_urls}')
