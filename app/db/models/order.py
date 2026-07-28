from __future__ import annotations

from enum import Enum
from uuid import UUID, uuid4
from decimal import Decimal
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .customer import Customer
    from .order_item import OrderItem
    from .payment import Payment

from sqlalchemy import Numeric, ForeignKey, Enum as SQLEnum, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

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
    
    customer: Mapped["Customer"] = relationship(
        "Customer",
        back_populates="orders",
        lazy="joined"
    )
    
    order_items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    payment: Mapped["Payment"] = relationship(
        "Payment",
        back_populates="order",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="joined"
    )
    
    def __repr__(self) -> str:
        return (
            f"Order("
            f"id={self.id}, "
            f"customer_id={self.customer_id}, "
            f"status='{self.status.value}', "
            f"total_price={self.total_price})"
        )