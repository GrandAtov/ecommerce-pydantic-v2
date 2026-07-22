from uuid import UUID, uuid4
from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.db.base import Base

class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True
    )
    
    brand: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    
    sku: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )
    
    price: Mapped[Decimal] = mapped_column(
        Numeric(10,2), 
        nullable=False
    )
    
    discount: Mapped[Decimal] = mapped_column(
        Numeric(5,2),
        default=0
    )
    
    stock: Mapped[int] = mapped_column(
        nullable=False,
        default=0
    )
    
    image_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )
    
    category_id: Mapped[UUID] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
        index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )