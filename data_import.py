import pandas as pd
from config import *
from sqlalchemy import create_engine

# Connect to MySQL database
engine = create_engine(mysql_path)

# Loading data into pandas DataFrame
# df1 = pd.read_csv("E:/RhaMo/CSV Files/Anime Dataset/anime_dataset_1.csv")
# df2 = pd.read_csv("E:/RhaMo/CSV Files/Anime Dataset/anime-2023-names.csv")
# df3 = pd.read_csv("E:/RhaMo/CSV Files/Anime Dataset/user_details.csv")
df4 = pd.read_csv("E:/RhaMo/CSV Files/Anime Dataset/final_animedataset.csv")

# Exporting DataFrame to MySQL
# df1.to_sql('anime_dataset', con=engine, if_exists='append', index=False)
# df2.to_sql('anime_genres', con=engine, if_exists='append', index=False)
# df3.to_sql('user_details', con=engine, if_exists='append', index=False)
df4.to_sql('final_data', con=engine, if_exists='append', index=False)
