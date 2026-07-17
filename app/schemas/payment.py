from uuid import UUID
from enum import Enum
from typing import Optional
from datetime import datetime

from types.common import PaymentAmount
from .base import BaseSchema
from .order import OrderResponse

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
    
class PaymentCreate(BaseSchema):
    order_id: UUID
    method: PaymentMethod
    
class PaymentUpdate(BaseSchema):
    status: Optional[PaymentStatus] = None
    paid_at: Optional[datetime] = None
 
class PaymentResponse(BaseSchema):
    id: UUID
    order: OrderResponse
    method: PaymentMethod
    status: PaymentStatus
    amount: PaymentAmount
    paid_at: Optional[datetime] = None
    created_at: datetime