from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models import Movie, Genre, Review


class MovieManager:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, title: str, release_year: int) -> Movie:
        movie = Movie(
            title= title,
            release_year= release_year
        )
        self.session.add(movie)
        self.session.commit()
        return movie
    
    def get(self, movie_id: int) -> Movie | None:
        return self.session.get(Movie, movie_id)

    def get_all(self):
        return list(self.session.execute(select(Movie)).scalars())

    def add_genre(self, movie_id: int, genre: Genre) -> Movie:
        movie = self.session.execute(select(Movie).where(Movie.id == movie_id)).scalar()
        movie.genres.append(genre)
        self.session.commit()
        return movie
    
    def get_reviews(self, movie_id: int):
        reviews = list(self.session.execute(select(Review).where(Review.movie_id == movie_id)).scalars())
        return reviews
    
    def get_average_rating(self, movie_id: int):
        score = self.session.execute(select(func.avg(Review.rating)).where(Review.movie_id == movie_id)).scalar_one_or_none()
        return score

    def update(self, movie_id: int, update_data: dict) -> Movie:
        result  = self.session.get(Movie, movie_id)
        if not result:
            return None
        for key, value in update_data.items():
            setattr(result, key, value)
        self.session.commit()
        return result

    def delete(self, movie_id: int) -> bool:
        result = self.session.get(Movie, movie_id)
        if not result:
            return False
        self.session.delete(result)
        self.session.commit()
        return True

    def remove_genre(self, movie_id: int, genre: Genre) -> Movie:
        result = self.session.get(Movie, movie_id)
        if not result:
            return None
        if genre in result.genres:
            result.genres.remove(genre)
        self.session.commit()
        return result

    def get_top_movies_by_rating(self, limit: int = 10) -> list[tuple]:
        return list(self.session.execute(select(Movie, func.avg(Review.rating)).join(Movie.reviews).group_by(Movie).order_by(func.avg(Review.rating).desc()).limit(limit)))
    

    def get_movies_by_genre(self, genre_name: str) -> list[Movie]:
        return list(self.session.execute(select(Movie).join(Movie.genres).where(Genre.name == genre_name)).scalars())

    def get_top_rated_movies_by_genre(self):
        result = select(Genre.name,Movie.title,func.avg(Review.rating).label("average_rating")).join(Genre.movies).join(Movie.reviews).group_by(Genre.name,Movie.title).order_by(func.avg(Review.rating).desc())
        result = result.subquery()
        top_rating = select(result.c.name,func.max(result.c.average_rating).label("max_rating")).group_by(result.c.name)
        top_rating = top_rating.subquery()
        final_result = select(result.c.name,result.c.title,result.c.average_rating).join(top_rating,(result.c.name == top_rating.c.name) & (result.c.average_rating == top_rating.c.max_rating)).order_by(result.c.name,result.c.average_rating.desc())
        return list(self.session.execute(final_result))