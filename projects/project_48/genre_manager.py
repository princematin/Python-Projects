from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from models import Genre, Movie


class GenreManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str) -> Genre:
        genre = Genre(name= name)
        self.session.add(genre)
        self.session.commit()
        return genre
        
    def get(self, genre_id: int) -> Genre | None:
        return self.session.execute(select(Genre).where(Genre.id == genre_id)).scalar_one_or_none()

    def get_all(self):
        return list(self.session.execute(select(Genre)).scalars())

    def get_genre_by_name(self, name: str) -> Genre | None:
        return self.session.execute(select(Genre).where(Genre.name == name)).scalar_one_or_none()

    def update(self, genre_id: int, new_name: str) -> Genre:
        result = self.session.get(Genre, genre_id)
        if not result:
            return None
        result.name = new_name
        self.session.commit()
        return result
    
    def delete(self, genre_id: int) -> bool:
        result = self.session.get(Genre, genre_id)
        if not result:
            return False
        self.session.delete(result)
        self.session.commit()
        return True

    def get_genres_with_most_movies(self) -> list[tuple]:
        return list(self.session.execute(select(Genre, func.count(Movie.id)).join(Genre.movies).group_by(Genre.id).order_by(func.count(Movie.id).desc())))