from uuid import UUID
from typing import Annotated, Optional
from datetime import datetime

from pydantic import Field, HttpUrl, model_validator

from .base import BaseSchema
from .category import Category

class Product(BaseSchema):
    id: UUID
    name: Annotated[str, Field(
        min_length=3,
        max_length=50
    )]
    brand: Annotated[str, Field(min_length=3)]
    description: Annotated[str, Field(
        min_length=10,
        max_length=500
    )]
    sku: Optional[str] = None
    price: Annotated[float, Field(gt=0)]
    discount: Annotated[float, Field(
        ge=0,
        le=100
    )]
    stock: Annotated[int, Field(ge=0)]
    image_url: HttpUrl
    category: Category
    created_at: datetime
    
    
    @model_validator(mode="before")
    def sku_validator(cls, data: dict) -> dict:
        if isinstance(data, dict) and not data.get("sku"):
            na = data.get("name", " ").replace(" ", "")[:3]
            br = data.get("brand", " ").replace(" ", "")[:3]
            de = data.get("description", " ").replace(" ", "")[:3]
            
            data["sku"] = f"PROD-{na}-{br}-{de}".upper()
        return data