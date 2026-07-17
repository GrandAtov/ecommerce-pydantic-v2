from uuid import UUID
from math import isclose
from typing import Literal

from pydantic import model_validator

from types.common import PositiveQuantity, OrderPrice, TotalPrice
from .base import BaseSchema
from .customer import CustomerResponse
from .product import ProductResponse

class OrderItemCreate(BaseSchema):
    product_id: UUID
    quantity: PositiveQuantity
    
class OrderItemResponse(BaseSchema):
    id: UUID
    product: ProductResponse
    quantity: PositiveQuantity
    price: OrderPrice
    
    
class OrderCreate(BaseSchema):
    customer_id: UUID
    items: list[OrderItemCreate]
    
class OrderResponse(BaseSchema):
    id: UUID
    customer: CustomerResponse
    items: list[OrderItemResponse]
    total_price: TotalPrice
    status: Literal[
        "pending",
        "paid",
        "shipped",
        "completed",
        "cancelled"
    ]
    