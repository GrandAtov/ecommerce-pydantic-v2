from enum import Enum
from uuid import UUID, uuid4
from decimal import Decimal
from datetime import datetime

from sqlalchemy import Numeric, ForeignKey, Enum as SQLEnum, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
    
class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    
class Order(Base):
    __tablename__ = "orders"
    
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
        
    customer_id: Mapped[UUID] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False,
        index=True
    )
    
    # items: list[OrderItem]
    
    total_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    
    status: Mapped[OrderStatus] = mapped_column(
        SQLEnum(OrderStatus),
        nullable=False,
        default=OrderStatus.PENDING,
        index=True
    )
    
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
    
    def __repr__(self) -> str:
        return (
            f"Order("
            f"id={self.id}, "
            f"customer_id={self.customer_id}, "
            f"status='{self.status.value}', "
            f"total_price={self.total_price})"
        )