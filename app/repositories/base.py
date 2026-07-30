from uuid import UUID
from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.base import Base

T = TypeVar("T", bound=Base)

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: type[T]):
        self.session = session
        self.model = model
        
    def create(self, obj: T) -> T:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj
    
    def get_by_id(self, obj_id: UUID) -> T | None:
        return self.session.get(self.model, obj_id)
    
    def get_all(self) -> list[T]:
        return list(
            self.session.execute(
                select(self.model)
            )
            .scalars()
            .all()
        )
        
    def update(self, obj: T) -> T:
        self.session.commit()
        self.session.refresh(obj)
        return obj
        
    def delete(self, obj: T) -> None:
        self.session.delete(obj)
        self.session.commit()