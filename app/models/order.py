from uuid import UUID
from math import isclose
from typing import Annotated, Literal

from pydantic import Field, model_validator

from .base import BaseSchema
from .customer import Customer
from .product import Product

class OrderItem(BaseSchema):
    id: UUID
    product: Product
    quantity: Annotated[int, Field(gt=0)]
    price: Annotated[float, Field(gt=0, strict=True)]
    
    @model_validator(mode="after")
    def price_validator(self):
        discount_price = self.product.price * ((100 - self.product.discount)/100)
        if not isclose(discount_price, self.price):
            raise ValueError("Harga item tidak sesuai dengan harga produk")
        
        if self.quantity > self.product.stock:
            raise ValueError("Jumlah pembelian melebihi stok produk")
        
        return self
    
    
class Order(BaseSchema):
    id: UUID
    customer: Customer
    items: list[OrderItem]
    total_price: float
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
        
        if not isclose(total, self.total_price):
            raise ValueError("Total harga semua item tidak valid")
        return self
    