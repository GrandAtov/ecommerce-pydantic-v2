from uuid import UUID

from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from app.db.models.product import Product
from app.repositories.base import BaseRepository

class ProductRepository(BaseRepository[Product]):
    def __init__(self, session: Session):
        super().__init__(session, Product)
        
    def find_by_sku(self, sku: str) -> Product | None:
        return (
            self.session.execute(
                select(self.model)
                .where(self.model.sku == sku)
            )
            .scalar_one_or_none()
        )
        
    def get_by_category(self, category_id: UUID) -> list[Product]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.category_id == category_id)
            )
            .scalars()
            .all()
        )
    
    def search(self, keyword: str) -> list[Product]:
        keyword = f"%{keyword}%"
        return list(
            self.session.execute(
                select(self.model)
                .where(or_(self.model.name.ilike(keyword), self.model.brand.ilike(keyword)))
            )
            .scalars()
            .all()
        )
        
    def get_available_products(self) -> list[Product]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.stock > 0)
            )
            .scalars()
            .all()
        )
        
    def get_latest(self) -> list[Product]:
        return list(
            self.session.execute(
                select(self.model)
                .order_by(
                    self.model.created_at.desc(),
                    self.model.id.desc()
                )
                .limit(10)
            )
            .scalars()
            .all()
        )