from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import Movie, Genre, Review


class MovieManager:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, title: str, release_year: int) -> Movie:
        pass

    def get(self, movie_id: int) -> Movie | None:
        pass

    def get_all(self):
        pass

    def add_genre(self, movie_id: int, genre: Genre) -> Movie:
        pass

    def get_reviews(self, movie_id: int):
        pass

    def get_average_rating(self, movie_id: int):
        pass
