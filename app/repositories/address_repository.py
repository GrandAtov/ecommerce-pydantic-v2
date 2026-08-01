from uuid import UUID

from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from app.db.models.address import Address
from app.repositories.base import BaseRepository

class AddressRepository(BaseRepository[Address]):
    def __init__(self, session: Session):
        super().__init__(session, Address)
        
    def find_by_city(self, city: str) -> list[Address]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.city == city)
            )
            .scalars()
            .all()
        )
    
    def find_by_province(self, province: str) -> list[Address]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.province == province)
            )
            .scalars()
            .all()
        )
        
    def find_by_customer(self, customer_id: UUID) -> list[Address]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.customer_id == customer_id)
            )
            .scalars()
            .all()
        )
    
    def search(self, keyword: str) -> list[Address]:
        keyword = f"%{keyword}%"
        return list(
            self.session.execute(
                select(self.model)
                .where(or_(
                    self.model.city.ilike(keyword),
                    self.model.province.ilike(keyword),
                    self.model.country.ilike(keyword)
                ))
            )
            .scalars()
            .all()
        )
        
    def find_by_name(self, name: str) -> Address | None:
        return (
            self.session.execute(
                select(self.model)
                .where(self.model.name == name)
            )
            .scalar_one_or_none()
        )