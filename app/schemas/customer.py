from uuid import UUID
from typing import Annotated, Optional
from datetime import datetime, date

from pydantic import Field, field_validator, EmailStr, SecretStr

from .base import BaseSchema
from .address import AddressCreate, AddressUpdate, AddressResponse

class CustomerCreate(BaseSchema):
    name: Annotated[str, Field(
        min_length=3,
        max_length=50
    )]
    email: EmailStr
    password: SecretStr
    phone: Annotated[str, Field(min_length=8)]
    birth_date: date
    address: AddressCreate
    
    
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
    
class CustomerUpdate(BaseSchema):
    name: Optional[Annotated[str, Field(
        min_length=3,
        max_length=50
    )]] = None
    email: Optional[EmailStr] = None
    password: Optional[SecretStr] = None
    phone: Optional[Annotated[str, Field(min_length=8)]] = None
    birth_date: Optional[date] = None
    address: Optional[AddressUpdate] = None
    is_active: Optional[bool] = None
    
    @field_validator("name")
    def name_validator(cls, value: str):
        if value is None:
            return value
        
        if not value.strip()    :
            raise ValueError("Nama tidak boleh hanya berisi spasi")
        return value
    
    @field_validator("password")
    def password_validator(cls, value: SecretStr) -> SecretStr:
        if value is None:
            return value
        
        password = value.get_secret_value()
        if len(password) < 8:
            raise ValueError("Password minimal 8 karakter")
        return value
    
    @field_validator("phone")
    def phone_validator(cls, value: str) -> str:
        if value is None:
            return value
        
        if " " in value:
            raise ValueError("Nomor telepon tidak boleh mengandung spasi")
        elif not value.isdigit():
            raise ValueError("Nomor telepon hanya berisi angka")
        return value
    

class CustomerResponse(BaseSchema):
    id: UUID
    name: str
    email: EmailStr
    phone: str
    birth_date: date
    address: AddressResponse
    registration_date: datetime
    is_active: bool = True