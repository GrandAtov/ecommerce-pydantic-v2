from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.order_item import OrderItem
from app.repositories.base import BaseRepository

class OrderItemRepository(BaseRepository[OrderItem]):
    def __init__(self, session: Session):
        super().__init__(session, OrderItem)
        
    def get_by_order(self, order_id: UUID) -> list[OrderItem]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.order_id == order_id)
            )
            .scalars()
            .all()
        )
    
    def get_by_product(self, product_id: UUID) -> list[OrderItem]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.product_id == product_id)
            )
            .scalars()
            .all()
        )