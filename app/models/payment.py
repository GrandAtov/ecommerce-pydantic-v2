from uuid import UUID
from enum import Enum
from math import isclose
from typing import Annotated, Optional
from datetime import datetime

from pydantic import Field, model_validator

from types.common import PaymentAmount
from .base import BaseSchema
from .order import Order

class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    BANK_TRANSFER = "bank_transfer"
    QRIS = "qris"
    CASH = "cash"
    
class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    REFUNDED = "refunded"
    
class Payment(BaseSchema):
    id: UUID
    order: Order
    method: PaymentMethod
    status: PaymentStatus
    amount: PaymentAmount
    paid_at: Optional[datetime] = None
    created_at: datetime
    
    @model_validator(mode="after")
    def payment_validator(self):
        if not isclose(self.order.total_price, self.amount):
            raise ValueError("Jumlah pembayaran tidak sesuai dengan order")
        
        if self.status == PaymentStatus.SUCCESS and self.paid_at is None:
            raise ValueError("Payment success harus memiliki waktu pembayaran")
        return self
    
    
    