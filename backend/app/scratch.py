from typing import Sequence
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import select, func
from app.models import Video
from itertools import groupby

sqlite_file_name = "database/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def select_genres() -> Sequence[str]:
    """ SELECT all videos from the database for quick access """
    with Session(engine) as session:
        statement = select(Video.genre).distinct()
        results = session.execute(statement).scalars().all()
        return results

def ordered() -> Sequence[Video]:
    with Session(engine) as session:
        statement = select(Video).order_by(Video.genre).where(Video.genre.is_not(None))
        res = session.exec(statement).all()
        # tuple(Video, )
        results = [vid[0] for vid in res]
        return results
# session.query(Table.column, 
#    func.count(Table.column)).group_by(Table.column).all()

if __name__ == "__main__":
    ord: Sequence[Video] = ordered()
    genre_dict = {}
    for key, group in groupby(ord, key=lambda vid: vid.genre):
            genre_dict[key] = list(group)
    print(genre_dict.keys())
