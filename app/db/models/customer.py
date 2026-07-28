from __future__ import annotations

from uuid import UUID, uuid4
from datetime import datetime, date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order
    from .address import Address

from app.db.base import Base

from sqlalchemy import String, Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
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
        index=True,
        unique=True
    )
    
    birth_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
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
    
    orders: Mapped[list["Order"]] = relationship(
        "Order",
        back_populates="customer",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    addresses: Mapped[list["Address"]] = relationship(
        "Address",
        back_populates="customer",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    def __repr__(self) -> str:
        return (
            "Customer("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"email='{self.email}', "
            f"phone='{self.phone}', "
            f"birth_date={self.birth_date}, "
            f"registration_date={self.registration_date}, "
            f"is_active={self.is_active})"
        )