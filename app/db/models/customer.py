from uuid import UUID, uuid4
from datetime import datetime, date

from app.db.base import Base

from sqlalchemy import String, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class Customer(Base):
    __tablename__ = "customers"
    
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True
    )
    
    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )
    
    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    phone: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    
    
    birth_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    
    address_id: Mapped[UUID] = mapped_column(
        ForeignKey("addresses.id"),
        nullable=False,
        index=True
    )
    
    registration_date: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )
    
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        index=True
    )