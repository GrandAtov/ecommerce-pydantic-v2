from uuid import UUID
from typing import Annotated

from pydantic import Field, field_validator

from app.models import BaseSchema

class Address(BaseSchema):
    id: UUID
    street: Annotated[str, Field(min_length=5)]
    city: Annotated[str, Field(min_length=3)]
    province: Annotated[str, Field(min_length=3)]
    postal_code: Annotated[str, Field(
        min_length=5,
        max_length=5
    )]
    country: Annotated[str, Field(min_length=3)]
    
    @field_validator("postal_code")
    def postal_code_validator(cls, value: str):
        if len(value) != 5 or not value.isdigit():
            raise ValueError("Kode pos harus terdiri dari 5 digit angka")
        return value