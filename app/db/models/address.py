from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Address(Base):
    __tablename__ = "addresses"
    
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
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
    
    def __repr__(self) -> str:
        return (
            "Address("
            f"id={self.id}, "
            f"street='{self.street}', "
            f"city='{self.city}', "
            f"province='{self.province}', "
            f"postal_code={self.postal_code}, "
            f"country='{self.country}'  "
            ")"
        )