from uuid import UUID, uuid4
from decimal import Decimal

from sqlalchemy import Numeric, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class OrderItem(Base):
    __tablename__ = "order_items"
    
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    
    order_id: Mapped[UUID] = mapped_column(
        ForeignKey("orders.id"),
        nullable=False,
        index=True
    )
    
    product_id: Mapped[UUID] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
        index=True
    )
    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1
    )
    
    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    
    def __repr__(self) -> str:
        return(
            "OrderItem("
            f"id={self.id}, "
            f"order_id={self.order_id}, "
            f"product_id={self.product_id}, "
            f"quantity={self.quantity}, "
            f"price={self.price})"
        )
    
