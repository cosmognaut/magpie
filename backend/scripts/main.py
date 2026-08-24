import asyncio
import pandas as pd
from pipeline.fetch import get_playlist_videos, get_videos_list
from app.models import Video
from app.database import insert_videos_to_db, create_db_and_tables, select_videos_from_db, add_genre
from typing import Sequence

async def get_videos():
    """ Fetches data from YouTube API and inserts that data into the database """
    incomplete_data = get_playlist_videos()
    complete_data = await get_videos_list(incomplete_data)
    return complete_data

def assign_genre_to_videos():
    """ Assigns genres to videos already present in the database """
    df: pd.DataFrame = pd.read_parquet('data/assigned_genres.parquet')
    def helper(row: pd.Series):
        video_id = str(row['id'])
        genre = str(row['genre'])
        add_genre(video_id, genre)
    df.apply(helper, axis=1)

def check_nothing_assigned():
    """ Checks if any videos in the database have no genre assigned to them. If yes, we assign it the Mixed Bag genre """
    # if any video does not have a genre yet, assign it to the Mixed Bag.
    videos: Sequence[Video] = select_videos_from_db()
    for video in videos:
        if video.genre == "":
            video = add_genre(str(video.id), "Mixed Bag")

if __name__ == "__main__":
    videos_list = asyncio.run(get_videos())
    create_db_and_tables()
    insert_videos_to_db(videos_list)
    assign_genre_to_videos()
    check_nothing_assigned()
