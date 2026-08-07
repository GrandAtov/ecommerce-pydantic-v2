from uuid import UUID

from app.services.base import BaseService

from app.repositories.customer_repository import CustomerRepository
from app.repositories.address_repository import AddressRepository

from app.db.models.address import Address
from app.db.models.customer import Customer

from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate
)

from app.schemas.address import (
    AddressCreate,
    AddressUpdate
)

class CustomerService(BaseService[CustomerRepository]):
    def __init__(self, customer_repository: CustomerRepository, address_repository: AddressRepository):
        super().__init__(customer_repository)
        
        self.address_repository = address_repository
    
    def create_customer(self, data: CustomerCreate) -> Customer:
        existing_email = self.repository.find_by_email(data.email)
        
        existing_phone = self.repository.find_by_phone(data.phone)
        
        if existing_email or existing_phone:
            raise ValueError("Email atau Nomor Telepon telah digunakan")

        
        customer = self.repository.create(
            Customer(
                name=data.name,
                email=data.email,
                password=data.password,
                phone=data.phone,
                birth_date=data.birth_date
            )
        )
        
        address = Address(
            name=data.address.name,
            street=data.address.street,
            city=data.address.city,
            province=data.address.province,
            postal_code=data.address.postal_code,
            country=data.address.country,
            customer_id=customer.id
        )
        
        self.address_repository.create(address)
        
        return customer
        
    def get_customer(self, customer_id: UUID) -> Customer:
        find_customer = self.repository.get_by_id(customer_id)
        
        if find_customer is None:
            raise ValueError("Customer tidak ditemukan")
        
        return find_customer
    
    def get_active_customers(self) -> list[Customer]:
        return self.repository.get_active_customers()
    
    def search(self, keyword: str) -> list[Customer]:
        return self.repository.search(keyword)
    
    def get_latest(self)  -> list[Customer]:
        return self.repository.get_latest()