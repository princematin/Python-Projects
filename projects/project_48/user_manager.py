from sqlalchemy import func, select
from sqlalchemy.orm import Session

from models import Review, User


class UserManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, email: str) -> User:
        user = User(
            name= name,
            email= email
        )
        self.session.add(user)
        self.session.commit()
        return user

    def get(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def get_all(self):
        return list(self.session.execute(select(User)).scalars())
        
    def get_user_by_email(self, email: str) -> User | None:
        return self.session.execute(select(User).where(User.email == email)).scalar_one_or_none()

    def get_most_active_users(self, limit=5):
        result = list(self.session.execute(select(Review.user_id, func.count(Review.user_id)).group_by(Review.user_id).order_by(func.count(Review.user_id).desc()).limit(limit)))
        return result
