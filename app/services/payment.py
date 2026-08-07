from uuid import UUID

from app.services.base import BaseService

from app.repositories.payment_repository import PaymentRepository
from app.repositories.order_repository import OrderRepository

from app.db.models.payment import Payment
from app.db.models.payment import PaymentStatus
from app.db.models.order import OrderStatus


from app.schemas.payment import (
    PaymentCreate,
    PaymentUpdate
)

class PaymentService(BaseService[PaymentRepository]):
    def __init__(self, payment_repository: PaymentRepository, order_repository: OrderRepository):
        super().__init__(payment_repository)
        
        self.order_repository = order_repository
    
    def create_payment(self, data: PaymentCreate) -> Payment:
        order = self.order_repository.get_by_id(data.order_id)
        
        if order is None:
            raise ValueError("Order tidak ditemukan")
        
        if order.status != OrderStatus.PENDING:
            raise ValueError("Order sudah dibayar atau tidak dapat di proses")
        
        payment = Payment(
            order_id=order.id,
            method=data.method,
            status=PaymentStatus.SUCCESS,
            amount=order.total_price
        )
        
        order.status = OrderStatus.PAID
            
        return self.repository.create(payment)
    
    def get_payment(self, payment_id: UUID) -> Payment:
        payment = self.repository.get_by_id(payment_id)
        
        if payment is None:
            raise ValueError("Payment tidak ditemukan")
        
        return payment
    
    def get_by_order(self, order_id: UUID) -> Payment:
        payment = self.repository.get_by_order(order_id)
        
        if payment is None:
            raise ValueError("Payment tidak ditemukan")
        
        return payment
            
    def get_by_status(self, status: PaymentStatus) -> list[Payment]:
        return self.repository.get_by_status(status)
    
    def get_latest(self) -> list[Payment]:
        return self.repository.get_latest()
    