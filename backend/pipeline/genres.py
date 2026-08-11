import pandas as pd
from app.database import add_genre 

df = pd.read_parquet('data/assigned_genres.parquet')
# the goal of this script would be to select videos from the database and manipulate the "genre" column based on the assigned genre by matching their id's with the ones in the parquet dataframe.
def helper(row: pd.Series):
    video_id = str(row['id'])
    genre = str(row['genre'])
    add_genre(video_id, genre)

df.apply(helper, axis=1)
