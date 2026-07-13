from uuid import UUID
from typing import Annotated
from datetime import datetime, date

from pydantic import Field, field_validator, EmailStr, SecretStr

from .base import BaseSchema
from .address import Address

class Customer(BaseSchema):
    id: UUID
    name: Annotated[str, Field(
        min_length=3,
        max_length=50
    )]
    email: EmailStr
    password: SecretStr
    phone: Annotated[str, Field(min_length=8)]
    birth_date: date
    address: Address
    registration_date: datetime = Field(default_factory=datetime.now)
    is_active: bool = True
    
    @field_validator("name")
    def name_validator(cls, value: str):
        if not value.strip()    :
            raise ValueError("Nama tidak boleh hanya berisi spasi")
        return value
    
    @field_validator("password")
    def password_validator(cls, value: SecretStr) -> SecretStr:
        password = value.get_secret_value()
        if len(password) < 8:
            raise ValueError("Password minimal 8 karakter")
        return value
    
    @field_validator("phone")
    def phone_validator(cls, value: str) -> str:
        if " " in value:
            raise ValueError("Nomor telepon tidak boleh mengandung spasi")
        elif not value.isdigit():
            raise ValueError("Nomor telepon hanya berisi angka")
        return value