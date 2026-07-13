from uuid import UUID
from typing import Annotated
from datetime import datetime

from pydantic import Field, HttpUrl

from .base import BaseSchema
from .category import Category

class Product(BaseSchema):
    id: UUID
    name: Annotated[str, Field(
        min_length=3,
        max_length=50
    )]
    description: Annotated[str, Field(
        min_length=10,
        max_length=500
    )]
    price: Annotated[float, Field(gt=0)]
    stock: Annotated[int, Field(ge=0)]
    image_url: HttpUrl
    category: Category
    created_at: datetime