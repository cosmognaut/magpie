import sqlite3
from .models import Video
from .database import get_ordered_videos 
from itertools import groupby
#
# with sqlite3.connect('database.db') as conn:
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM video')
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     cur.close()
#
# def check_if_video_None():
#     with sqlite3.connect('database.db') as conn:
#         cur = conn.cursor()
#         cur.execute('SELECT * FROM video')
#         row = cur.fetchone()
#         # cast this into a Video object
#         fetched_video = Video(id=row[0], title=row[1], channel_name=row[2], duration=row[3], description=row[4], published_at=row[5], view_count=row[6], thumbnail_link=row[7], watched=row[8], liked=row[9], embeddings=row[10], categories=row[11])
#         print(fetched_video)
#         print(type(fetched_video.embeddings))
#         print(type(fetched_video.categories))
#         if fetched_video.embeddings is None:
#             print("You're good to go.")
#         cur.close()
#

if __name__ == "__main__":
    ordered_vids = get_ordered_videos()
    genre_dict = {}
    for key, group in groupby(ordered_vids, key=lambda video: video.genre):
            genre_dict[key] = list(group)
    print(genre_dict.keys())
    print(len(genre_dict))
