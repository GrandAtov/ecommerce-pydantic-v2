from __future__ import annotations

from uuid import UUID, uuid4
from enum import Enum
from datetime import datetime
from decimal import Decimal
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order

from sqlalchemy import Enum as SQLEnum, Numeric, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    BANK_TRANSFER = "bank_transfer"
    QRIS = "qris"
    CASH = "cash"
    
class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    REFUNDED = "refunded"
    
class Payment(Base):
    __tablename__ = "payments"
    
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    
    order_id: Mapped[UUID] = mapped_column(
        ForeignKey("orders.id"),
        unique=True,
        nullable=False,
        index=True
    )
    
    method: Mapped[PaymentMethod] = mapped_column(
        SQLEnum(PaymentMethod),
        nullable=False
    )
    
    status: Mapped[PaymentStatus] = mapped_column(
        SQLEnum(PaymentStatus),
        nullable=False,
        default=PaymentStatus.PENDING
    )
    
    amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    
    paid_at: Mapped[Optional[datetime]] = mapped_column(
        nullable=True
    )
    
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )
    
    order: Mapped["Order"] = relationship(
        "Order",
        back_populates="payment",
        lazy="joined"
    )
    
    def __repr__(self) -> str:
        return(
            "Payment("
            f"id={self.id}, "
            f"order_id={self.order_id}, "
            f"method='{self.method.value}', "
            f"status='{self.status.value}', "
            f"amount={self.amount}, "
            f"paid_at={self.paid_at}, "
            f"created_at={self.created_at})"
        )