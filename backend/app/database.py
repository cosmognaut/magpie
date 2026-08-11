from typing import Sequence
from sqlmodel import SQLModel, Session, create_engine, select
from app.models import Video

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    """ CREATE the initial setup for the database """
    SQLModel.metadata.create_all(engine)

def insert_videos_to_db(video_list: list[Video]):
    """ INSERT each video from a video list into the database """
    with Session(engine) as session:
        for video in video_list:
            session.add(video)
        session.commit()

def select_videos_from_db() -> Sequence[Video]:
    """ SELECT all videos from the database for quick access """
    with Session(engine) as session:
        statement = select(Video)
        results = session.exec(statement)
        return results.all()

def add_genre(video_id: str, genre: str) -> Video:
    """ UPDATE a single Video record in the database and return the updated object """
    with Session(engine) as session:
        statement = select(Video).where(Video.id == video_id)
        found_video = session.exec(statement).one()
        found_video.genre = genre
        session.add(found_video)
        session.commit()
        session.refresh(found_video)
        return found_video

def get_genres() -> set[str]:
    """ Return all genres present in the database """
    videos = select_videos_from_db()
    genres: list = [video.genre for video in videos]
    return set(genres)

def get_genre_videos(genre: str) -> Sequence[Video]:
    """ Return all videos belonging to a particular genre """
    with Session(engine) as session:
        statement = select(Video).where(Video.genre == genre)
        found = session.exec(statement).all()
        return found
