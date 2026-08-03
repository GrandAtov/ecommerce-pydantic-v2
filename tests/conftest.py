# tests/conftest.py
from decimal import Decimal
from datetime import date
import pytest
from sqlalchemy import create_engine, event, text  # ✅ Tambahkan text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from app.db.base import Base
from app.db.models import (
    Category,
    Product,
    Customer,
    Address,
    Order,
    OrderItem,
    Payment,
)

TEST_DATABASE_URL = "sqlite:///:memory:"

# ✅ Cara 1: Event listener (Recommended)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

engine = create_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def session():
    """Create test session with in-memory database"""
    Base.metadata.create_all(engine)
    session = TestingSessionLocal()
    
    # ✅ Cara 2: Pastikan foreign key aktif (opsional, karena sudah di event listener)
    # Tapi tetap aman untuk dipanggil
    session.execute(text("PRAGMA foreign_keys=ON"))
    
    yield session
    
    session.close()
    Base.metadata.drop_all(engine)


# Fixtures tetap sama
@pytest.fixture
def category(session):
    category = Category(
        name="Keyboard",
        description="Mechanical Keyboard",
        is_active=True,
    )
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


@pytest.fixture
def product(session, category):
    product = Product(
        name="Keyboard RGB",
        brand="Logitech",
        description="Gaming Keyboard",
        sku="KB0011",
        price=Decimal("1000000"),
        discount=Decimal("10"),
        stock=10,
        image_url="https://example.com/image.jpg",
        category_id=category.id,
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@pytest.fixture
def customer(session):
    customer = Customer(
        name="Grand",
        email="grand@test.com",
        password="hashed_password",
        phone="08123456789",
        birth_date=date(2005, 1, 1),
    )
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@pytest.fixture
def address(session, customer):
    address = Address(
        name="Rumah",
        street="Jl. Merdeka",
        city="Pontianak",
        province="Kalbar",
        postal_code="78111",
        country="Indonesia",
        customer_id=customer.id,
    )
    session.add(address)
    session.commit()
    session.refresh(address)
    return address


@pytest.fixture
def order(session, customer):
    order = Order(
        customer_id=customer.id,
        total_price=Decimal("1000000"),
    )
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


@pytest.fixture
def order_item(session, order, product):
    item = OrderItem(
        order_id=order.id,
        product_id=product.id,
        quantity=2,
        price=Decimal("900000"),
    )
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@pytest.fixture
def payment(session, order):
    payment = Payment(
        order_id=order.id,
        method="qris",
        status="pending",
        amount=Decimal("1000000"),
    )
    session.add(payment)
    session.commit()
    session.refresh(payment)
    return payment


# ✅ Fixture tambahan untuk test yang butuh data clean
@pytest.fixture
def clean_customer(session):
    """Create customer WITHOUT any relations (no addresses, no orders)"""
    customer = Customer(
        name="Clean Customer",
        email="clean@test.com",
        password="hashed_password",
        phone="08987654321",
        birth_date=date(2000, 1, 1),
    )
    session.add(customer)
    session.commit()
    session.refresh(customer)
    
    # Pastikan tidak ada relasi
    assert len(customer.addresses) == 0
    assert len(customer.orders) == 0
    
    return customer


@pytest.fixture
def clean_order(session, clean_customer):
    """Create order tanpa relasi"""
    order = Order(
        customer_id=clean_customer.id,
        total_price=Decimal("500000"),
    )
    session.add(order)
    session.commit()
    session.refresh(order)
    return order