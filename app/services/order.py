from uuid import UUID

from decimal import Decimal

from app.services.base import BaseService

from app.repositories.order_repository import OrderRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.customer_repository import CustomerRepository


from app.db.models.order import Order, OrderStatus
from app.db.models.order_item import OrderItem
from app.db.models.product import Product

from app.schemas.order import OrderCreate

class OrderService(BaseService[OrderRepository]):
    def __init__(self, order_repository: OrderRepository, product_repository: ProductRepository, customer_repository: CustomerRepository):
        super().__init__(order_repository)
        
        self.product_repository = product_repository
        self.customer_repository = customer_repository
        
    def create_order(self, data: OrderCreate) -> Order:
        existing_customer = self.customer_repository.get_by_id(data.customer_id)
        
        if existing_customer is None:
            raise ValueError("Customer Tidak Ditemukan")
        
        valid_product: list[Product] = []
        
        for item in data.items:
            product = self.product_repository.get_by_id(item.product_id)
            
            if product is None:
                raise ValueError("Produk tidak ditemukan")
            
            valid_product.append(product)
        
        total_price = Decimal("0")
        order_items: list[OrderItem] = []
        for product, item in zip(valid_product, data.items): 
            if product.stock < item.quantity:
                raise ValueError("Stok produk tidak mencukupi")
            
            
            final_price = (
                product.price * 
                (Decimal("100") - product.discount)
                / Decimal("100"))
            
            subtotal = final_price * item.quantity
            
            
            order_items.append(
                OrderItem(
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price=final_price
                )
            )
            
            total_price += subtotal
        
        return self.repository.create(
            Order(
                customer_id=data.customer_id,
                items=order_items,
                total_price=total_price
            )
        )
    
    def get_order(self, order_id: UUID) -> Order:
        existing_order = self.repository.get_by_id(order_id)
        
        if existing_order is None:
            raise ValueError("Order tidak ditemukan")
        
        return existing_order
    
    def get_by_customer(self, customer_id: UUID) -> list[Order]:
        return self.repository.get_by_customer(customer_id)
    
    def get_by_status(self, status: OrderStatus) -> list[Order]:
        return self.repository.get_by_status(status)
    
    def get_latest(self) -> list[Order]:
        return self.repository.get_latest()
    
    def get_order_detail(self, order_id: UUID) -> Order:
        order = self.repository.get_detail_by_id(order_id)
        
        if order is None:
            raise ValueError("Order Tidak Ditemukan")
        
        return order
