import pytest

from app.models import (
    Category,
    Product,
    Address,
    Customer,
    OrderItem,
    Order
)


@pytest.fixture
def order():

    category = Category(
        id="550e8400-e29b-41d4-a716-446655440001",
        name="Keyboard",
        description="Mechanical gaming keyboard",
        created_at="2026-07-13T20:00:00"
    )


    product = Product(
        id="550e8400-e29b-41d4-a716-446655440010",
        name="Keyboard RGB",
        brand="Logitech",
        description="Mechanical keyboard gaming",
        price=100000,
        discount=10,
        stock=5,
        image_url="https://example.com/image.jpg",
        category=category,
        created_at="2026-07-13T21:00:00"
    )


    address = Address(
        id="8b091986-5a63-4110-90bc-6cef8197b493",
        street="Dinasti Indah",
        city="Pontianak",
        province="Kalimantan Barat",
        postal_code="71857",
        country="Indonesia"
    )


    customer = Customer(
        id="b46e153a-2cfd-4e9f-ab14-9e09506c544d",
        name="Grand Atov",
        email="grand@gmail.com",
        password="12345678",
        phone="0899123456",
        birth_date="2007-09-20",
        address=address
    )


    item = OrderItem(
        id="29bb065c-64cf-4f3a-a3b6-426c174317ba",
        product=product,
        quantity=2,
        price=90000
    )


    return Order(
        id="dff581fd-6959-4d89-8400-ce5f4202c6ec",
        customer=customer,
        items=[item],
        total_price=180000,
        status="paid"
    )
    
@pytest.fixture
def category():

    return Category(
        id="550e8400-e29b-41d4-a716-446655440001",
        name="Keyboard",
        description="Mechanical gaming keyboard",
        created_at="2026-07-13T20:00:00"
    )


@pytest.fixture
def product(category):

    return Product(
        id="550e8400-e29b-41d4-a716-446655440010",
        name="Keyboard RGB",
        brand="Logitech",
        description="Mechanical keyboard gaming",
        price=100000,
        discount=10,
        stock=10,
        image_url="https://example.com/image.jpg",
        category=category,
        created_at="2026-07-13T21:00:00"
    )


@pytest.fixture
def address():

    return Address(
        id="8b091986-5a63-4110-90bc-6cef8197b493",
        street="Dinasti Indah",
        city="Pontianak",
        province="Kalimantan Barat",
        postal_code="71857",
        country="Indonesia"
    )


@pytest.fixture
def customer(address):

    return Customer(
        id="b46e153a-2cfd-4e9f-ab14-9e09506c544d",
        name="Grand Atov",
        email="grand@gmail.com",
        password="12345678",
        phone="0899123456",
        birth_date="2007-09-20",
        address=address
    )