# Anime Recommendation App

## About

This application will be used to recommend anime to not just traditional and new anime watchers, but to those who have yet to get into it. The app will select
anime you should watch depending on anime you may have watched previously, as well as anime you plan on watching.
If you haven't wathced any anime, you can select genres you are interested in and a recommendation will be made on that. It can aslo make a recommendation
movies and shows you have watched or liked that are not anime based on that movie or shows genre. You will be able to add anime to your favorites
and anything in your favorites, other anime will be recommended to you based on those anime's genre.

-Recommendarion on wether you wamt to watch movies, short anime, and or longer anime

-Will show the viusal analystical data for most popular anime

-Will have visual analytics on the top rated anime

-Favorites list and Save later list

-User profile to save your favorites and save later options

-The tools I will use are Python, Pandas, JHipster, HTML, CSS, and MySQL


## Datasets

The dataset I will be using to help with my analysis is from kaggle, _Anime Dataset 2023_.
I will use the csv files `anime-dataset-2023.csv` and `user-details-2023.csv` to look
at analytical data for anime trends and see who is mainly interested in what

### Content

*anime-dataset-2023.csv*

- `anime_id`: Unique ID for each anime.
- `Name`: The name of the anime in its original language.
- `English` name: The English name of the anime.
- `Other name`: Native name or title of the anime(can be in Japanese, Chinese or Korean).
- `Score`: The score or rating given to the anime.
- `Genres`: The genres of the anime, separated by commas.
- `Synopsis`: A brief description or summary of the anime's plot.
- `Type`: The type of the anime (e.g., TV series, movie, OVA, etc.).
- `Episodes`: The number of episodes in the anime.
- `Aired`: The dates when the anime was aired.
- `Premiered`: The season and year when the anime premiered.
- `Status`: The status of the anime (e.g., Finished Airing, Currently Airing, etc.).
- `Producers`: The production companies or producers of the anime.
- `Licensors`: The licensors of the anime (e.g., streaming platforms).
- `Studios`: The animation studios that worked on the anime.
- `Source`: The source material of the anime (e.g., manga, light novel, original).
- `Duration`: The duration of each episode.
- `Rating`: The age rating of the anime.
- `Rank`: The rank of the anime based on popularity or other criteria.
- `Popularity`: The popularity rank of the anime.
- `Favorites`: The number of times the anime was marked as a favorite by users.
- `Scored By`: The number of users who scored the anime.
- `Members`: The number of members who have added the anime to their list on the platform.
- `Image URL`: The URL of the anime's image or poster.


*users-details-2023.csv*

- `Mal ID`: Unique ID for each user.
- `Username`: The username of the user.
- `Gender`: The gender of the user.
- `Birthday`: The birthday of the user (in ISO format).
- `Location`: The location or country of the user.
- `Joined`: The date when the user joined the platform (in ISO format).
- `Days Watched`: The total number of days the user has spent watching anime.
- `Mean Score`: The average score given by the user to the anime they have watched.
- `Watching`: The number of anime currently being watched by the user.
- `Completed`: The number of anime completed by the user.
- `On Hold`: The number of anime on hold by the user.
- `Dropped`: The number of anime dropped by the user.
- `Plan to Watch`: The number of anime the user plans to watch in the future.
- `Total Entries`: The total number of anime entries in the user's list.
- `Rewatched`: The number of anime rewatched by the user.
- `Episodes Watched`: The total number of episodes watched by the user.
