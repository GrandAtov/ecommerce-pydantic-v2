from uuid import UUID
from enum import Enum
from typing import Annotated, Optional
from datetime import datetime

from pydantic import Field, model_validator

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
    amount: Annotated[float, Field(gt=0)]
    paid_at: Optional[datetime] = None
    created_at: datetime
    
    @model_validator(mode="after")
    def payment_validator(self):
        if self.status == PaymentStatus.SUCCESS and self.paid_at is None:
            raise ValueError("Payment succes harus memiliki waktu pembayaran")
        return self
    
    
    