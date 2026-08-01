from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.payment import Payment, PaymentStatus
from app.repositories.base import BaseRepository

class PaymentRepository(BaseRepository[Payment]):
    def __init__(self, session: Session):
        super().__init__(session, Payment)
        
    def get_by_order(self, order_id: UUID) -> Payment | None:
        return (
            self.session.execute(
                select(self.model)
                .where(self.model.order_id == order_id)
            )
            .scalar_one_or_none()
        )
        
    def get_by_status(self, status: PaymentStatus) -> list[Payment]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.status == status)
            )
            .scalars()
            .all()
        )
    
    def get_latest(self) -> list[Payment]:
        return list(
            self.session.execute(
                select(self.model)
                .order_by(self.model.created_at.desc())
                .limit(10)
            )
            .scalars()
            .all()
        )