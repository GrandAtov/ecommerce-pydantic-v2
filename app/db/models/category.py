from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.db.base import Base

class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[UUID] = mapped_column(
        primary_key=True, 
        default=uuid4
    )
    
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )
    
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True)
    
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()        
    )
    
    def __repr__(self) -> str:
        return ( 
            "Category("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"description='{self.description}', "
            f"is_active={self.is_active}, "
            f"created_at={self.created_at}"
            ")"
        )