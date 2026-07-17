from uuid import UUID
from typing import Annotated, Optional
from datetime import datetime

from pydantic import Field, HttpUrl, model_validator

from types.common import PositivePrice, PositiveStock
from .base import BaseSchema


class ProductCreate(BaseSchema):
    name: Annotated[str, Field(
        min_length=3,
        max_length=50
    )]
    brand: Annotated[str, Field(min_length=3)]
    description: Annotated[str, Field(
        min_length=10,
        max_length=500
    )]
    price: PositivePrice
    discount: Annotated[float, Field(
        ge=0,
        le=100
    )]
    stock: PositiveStock
    image_url: HttpUrl
    category_id: UUID


class ProductUpdate(BaseSchema):
    name: Optional[Annotated[str, Field(
        min_length=3,
        max_length=50
    )]] = None
    brand: Optional[Annotated[str, Field(min_length=3)]] = None
    description: Optional[Annotated[str, Field(
        min_length=10,
        max_length=500
    )]] = None
    price: Optional[PositivePrice] = None
    discount: Optional[Annotated[float, Field(
        ge=0,
        le=100
    )]] = None
    stock: Optional[PositiveStock] = None
    image_url: Optional[HttpUrl] = None
    category_id: Optional[UUID] = None
    
    
class ProductResponse(BaseSchema):
    id: UUID
    name: str
    brand: str
    description: str
    price: PositivePrice
    discount: float
    stock: PositiveStock
    sku: str
    image_url: HttpUrl
    category_id: UUID
    created_at: datetime