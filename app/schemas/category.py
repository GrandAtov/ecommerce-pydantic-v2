from datetime import datetime
from uuid import UUID
from typing import Annotated, Optional

from pydantic import Field

from .base import BaseSchema

class CategoryCreate(BaseSchema):
    name: Annotated[str, Field(
        min_length=3,
        max_length=30
    )]
    description: Annotated[str, Field(
        min_length=10,
        max_length=200
    )]
    is_active: bool = True
    
class CategoryUpdate(BaseSchema):
    name: Optional[Annotated[str, Field(
        min_length=3,
        max_length=30
    )]] = None
    description: Optional[Annotated[str, Field(
        min_length=10,
        max_length=200
    )]] = None
    is_active: Optional[bool] = None
    
class CategoryResponse(BaseSchema):
    id: UUID
    name: str
    description: str
    is_active: bool
    created_at: datetime