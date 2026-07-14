import pytest

from pydantic import ValidationError

from app.models import Customer



def test_customer_success(customer):

    assert customer.email == "grand@gmail.com"



def test_customer_name_only_space(address):

    with pytest.raises(ValidationError):

        Customer(
            id="b46e153a-2cfd-4e9f-ab14-9e09506c544d",
            name="     ",
            email="grand@gmail.com",
            password="12345678",
            phone="0899123456",
            birth_date="2007-09-20",
            address=address
        )



def test_customer_password_too_short(address):

    with pytest.raises(ValidationError):

        Customer(
            id="b46e153a-2cfd-4e9f-ab14-9e09506c544d",
            name="Grand",
            email="grand@gmail.com",
            password="123",
            phone="0899123456",
            birth_date="2007-09-20",
            address=address
        )



def test_customer_phone_contains_space(address):

    with pytest.raises(ValidationError):

        Customer(
            id="b46e153a-2cfd-4e9f-ab14-9e09506c544d",
            name="Grand",
            email="grand@gmail.com",
            password="12345678",
            phone="0899 123",
            birth_date="2007-09-20",
            address=address
        )



def test_customer_phone_not_number(address):

    with pytest.raises(ValidationError):

        Customer(
            id="b46e153a-2cfd-4e9f-ab14-9e09506c544d",
            name="Grand",
            email="grand@gmail.com",
            password="12345678",
            phone="abc123",
            birth_date="2007-09-20",
            address=address
        )



def test_invalid_email(address):

    with pytest.raises(ValidationError):

        Customer(
            id="b46e153a-2cfd-4e9f-ab14-9e09506c544d",
            name="Grand",
            email="email-salah",
            password="12345678",
            phone="0899123456",
            birth_date="2007-09-20",
            address=address
        )