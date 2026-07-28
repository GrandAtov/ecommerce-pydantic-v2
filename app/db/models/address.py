from __future__ import annotations

from uuid import UUID, uuid4
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .customer import Customer

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Address(Base):
    __tablename__ = "addresses"
    
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    street: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    city: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    
    province: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    
    postal_code: Mapped[str] = mapped_column(
        String(5),
        nullable=False,
        index=True
    )
    
    country: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    
    customer_id: Mapped[UUID] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False,
        index=True
    )
    
    customer: Mapped["Customer"] = relationship(
        "Customer",
        back_populates="addresses",
        lazy="joined"
    ) 
    
    def __repr__(self) -> str:
        return (
            "Address("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"street='{self.street}', "
            f"city='{self.city}', "
            f"province='{self.province}', "
            f"postal_code='{self.postal_code}', "
            f"country='{self.country}'  "
            ")"
        )