from uuid import UUID
from typing import Annotated, Optional

from pydantic import Field, field_validator

from .base import BaseSchema

class AddressCreate(BaseSchema):
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

class AddressUpdate(BaseSchema):
    street: Optional[Annotated[str, Field(min_length=5)]] = None
    city: Optional[Annotated[str, Field(min_length=3)]] = None
    province: Optional[Annotated[str, Field(min_length=3)]] = None
    postal_code: Optional[Annotated[str, Field(
        min_length=5,
        max_length=5
    )]] = None
    country: Optional[Annotated[str, Field(min_length=3)]] = None
    
    @field_validator("postal_code")
    def postal_code_validator(cls, value: str):
        if value == None:
            return value
        
        if len(value) != 5 or not value.isdigit():
            raise ValueError("Kode pos harus terdiri dari 5 digit angka")
        return value
    
class AddressResponse(BaseSchema):
    id: UUID
    street: str
    city: str
    province: str
    postal_code: str
    country: str