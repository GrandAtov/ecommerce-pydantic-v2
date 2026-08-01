from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.order import Order, OrderStatus
from app.repositories.base import BaseRepository

class OrderRepository(BaseRepository[Order]):
    def __init__(self, session: Session):
        super().__init__(session, Order)
        
    def get_by_customer(self, customer_id: UUID) -> list[Order]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.customer_id == customer_id)
            )
            .scalars()
            .all()
        )
    
    def get_by_status(self, status: OrderStatus) -> list[Order]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.status == status)
            )
            .scalars()
            .all()
        )
        
    def get_latest(self) -> list[Order]:
        return list(
            self.session.execute(
                select(self.model)
                .order_by(self.model.created_at.desc())
                .limit(10)
            )
            .scalars()
            .all()
        )
        
    def get_detail_by_id(self, order_id: UUID) -> Order | None:
        return (
            self.session.execute(
                select(self.model)
                .where(self.model.id == order_id)
            )
            .scalar_one_or_none()
        )