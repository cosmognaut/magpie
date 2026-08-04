import csv
from app.database import select_videos_from_db

with open('video.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['id', 'title', 'channel_name', 'duration', 'description', 'category', 'published_at', 'view_count', 'embeddings', 'tags']) # omitting thumbnail_link, watched and liked fields because those are not relevant.
    videos = select_videos_from_db()
    for video in videos:
        writer.writerow([f'{video.id}', f'{video.title}', f'{video.channel_name}', f'{video.duration}', f'{video.description}', f'{video.category}', f'{video.published_at}', f'{video.view_count}', f'{video.embeddings}', f'{video.tags}'])
