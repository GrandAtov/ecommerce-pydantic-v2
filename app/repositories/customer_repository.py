from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from app.db.models.customer import Customer
from app.repositories.base import BaseRepository

class CustomerRepository(BaseRepository[Customer]):
    def __init__(self, session: Session):
        super().__init__(session, Customer)
        
    def find_by_email(self, email: str) -> Customer | None:
        return (
            self.session.execute(
                select(self.model)
                .where(self.model.email == email)
            )
            .scalar_one_or_none()
        )
    
    def find_by_phone(self, phone: str) -> Customer | None:
        return (
            self.session.execute(
                select(self.model)
                .where(self.model.phone == phone)
            )
            .scalar_one_or_none()
        )
    
    def search(self, keyword: str) -> list[Customer]:
        keyword = f"%{keyword}%"
        return list(
            self.session.execute(
                select(self.model)
                .where(or_(self.model.name.ilike(keyword),self.model.email.ilike(keyword)))
            )
            .scalars()
            .all()
        )
        
    def get_active_customers(self) -> list[Customer]:
        return list(
            self.session.execute(
                select(self.model)
                .where(self.model.is_active.is_(True))
            )
            .scalars()
            .all()
        )
    
    def get_latest(self) -> list[Customer]:
        return list(
            self.session.execute(
                select(self.model)
                .order_by(
                    self.model.registration_date.desc(),
                    self.model.id.desc()
                )
                .limit(10)
            )
            .scalars()
            .all()
        )


