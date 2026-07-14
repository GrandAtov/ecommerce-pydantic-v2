from datetime import datetime
from uuid import UUID
from typing import Annotated

from pydantic import Field

from .base import BaseSchema

class Category(BaseSchema):
    id: UUID
    name: Annotated[str, Field(
        min_length=3,
        max_length=30
    )]
    description: Annotated[str, Field(
        min_length=10,
        max_length=200
    )]
    is_active: bool = True
    created_at: datetime