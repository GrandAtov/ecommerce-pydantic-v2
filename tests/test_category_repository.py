from app.db.session import SessionLocal

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.category import Category
from app.repositories.base import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: Session):
        super().__init__(session, Category)
        
    def find_by_name(self, name: str) -> Category | None:
        return ( 
            self.session.execute(
                select(self.model)
                .where(Category.name == name)
            )
            .scalar_one_or_none()
        )

    def get_active_categories(self) -> list[Category]:
        return list(
            self.session.execute(
                select(self.model)
                .where(Category.is_active.is_(True))
            )
            .scalars()
            .all()
        )

        
        
session = SessionLocal()

CategoryRepository.create()