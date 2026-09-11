from sqlalchemy import func, select
from sqlalchemy.orm import Session

from models import Review


class ReviewManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, movie_id: int, user_id: int, rating: int, comment: str = None) -> Review:
        review = Review(
            movie_id= movie_id,
            user_id= user_id,
            rating= rating,
            comment= comment
        )
        self.session.add(review)
        self.session.commit()
        return review
    
    def get(self, review_id: int) -> Review | None:
        return self.session.get(Review, review_id)
        
    def get_all(self):
        return list(self.session.execute(select(Review)).scalars())

    def get_reviews_by_user(self, user_id: int):
        return list(self.session.execute(select(Review).where(Review.user_id == user_id)).scalars())

    def get_latest_reviews_for_movie_by_time(self, movie_id: int, limit: int = 5):
        return list(self.session.execute(select(Review).where(Review.movie_id == movie_id).order_by((Review.created_at).desc()).limit(limit)).scalars())
     
    def get_highest_rated_reviews(self, movie_id: int, limit: int = 5):
        return list(self.session.execute(select(Review).where(Review.movie_id == movie_id).order_by((Review.rating).desc()).limit(limit)).scalars())

    def get_average_rating_by_user(self):
        return list(self.session.execute(select(Review.user_id, func.avg(Review.rating)).group_by(Review.user_id)))

    def update(self, review_id: int, update_data: dict) -> Review:
        pass

    def delete(self, review_id: int) -> bool:
        pass
