from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_genres, get_genre_videos

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}

app.frontend("/", directory="dist")

origins = [
    'http://localhost:5173', # for development
    'https://magpie.ishu.foo/', # main URL
    'https://magpie.fastapicloud.dev' # alternative URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/videos/")
async def get_videos():
    genres = sorted(get_genres())
    final_dict = {}
    for genre in genres:
        genre_video_list = get_genre_videos(genre)
        final_dict[genre] = genre_video_list
    return final_dict

# @app.get("/videos/")
# async def get_videos():
    # df = pd.read_parquet('assigned_genres.parquet')
    # genre_list = list(df['genre'].unique())
    # return_dict = {}
    #
    # for genre in genre_list:
    #     genre_videos = []
    #     filtered_df = df[df['genre'] == genre]
    #     for idx, data in filtered_df.iterrows():
    #         video_dict = {}
    #         if pd.isna(data.id):
    #             video_dict['id'] = None 
    #         else:
    #             video_dict['id'] = data.id
    #         if pd.isna(data.title):
    #             video_dict['title'] = None 
    #         else:
    #             video_dict['title'] = data.title
    #         if pd.isna(data.channel_name):
    #             video_dict['channel_name'] = None 
    #         else:
    #             video_dict['channel_name'] = data.channel_name
    #         if pd.isna(data.duration):
    #             video_dict['duration'] = None 
    #         else:
    #             video_dict['duration'] = data.duration
    #         if pd.isna(data.description):
    #             video_dict['description'] = None 
    #         else:
    #             video_dict['description'] = data.description
    #         if pd.isna(data.published_at):
    #             video_dict['published_at'] = None 
    #         else:
    #             video_dict['published_at'] = data.published_at
    #         if pd.isna(data.view_count):
    #             video_dict['view_count'] = None 
    #         else:
    #             video_dict['view_count'] = data.view_count
    #         if pd.isna(data.genre):
    #             video_dict['genre'] = None 
    #         else:
    #             video_dict['genre'] = data.genre
    #         genre_videos.append(video_dict)
    #     return_dict[genre] = genre_videos
    #
    # return return_dict 
    #
# now do this exact same thing, but with the database, without touching the parquet file.
