from sqlalchemy import func, select
from sqlalchemy.orm import Session

from models import Review, User


class UserManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, email: str) -> User:
        pass

    def get(self, user_id: int) -> User | None:
        pass

    def get_all(self):
        pass
        
    def get_user_by_email(self, email: str) -> User | None:
        pass

    def get_most_active_users(self, limit=5):
        pass
