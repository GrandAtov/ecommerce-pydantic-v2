from uuid import UUID
from typing import Annotated, Literal

from pydantic import Field, model_validator

from app.models import BaseSchema, Customer, Product

class OrderItem(BaseSchema):
    id: UUID
    product: Product
    quantity: Annotated[int, Field(gt=0)]
    price: Annotated[float, Field(gt=0)]
    
class Order(BaseSchema):
    id: UUID
    customer: Customer
    items: list[OrderItem]
    status: Literal[
        "pending",
        "paid",
        "shipped",
        "completed",
        "cancelled"
    ]
    
    @model_validator(mode="after")
    def order_validator(self):
        if not self.items:
            raise ValueError("Order harus memiliki minimal satu item")
        
        total = sum(
            item.quantity * item.price
            for item in self.items
        )
        
        if total <= 0:
            raise ValueError("Total harga semua item tidak valid")
        return self
    