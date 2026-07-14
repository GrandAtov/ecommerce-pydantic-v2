import pytest

from app.models import Product, Category, OrderItem, Order, Payment, PaymentStatus


def create_product():

    category = Category(
        id="550e8400-e29b-41d4-a716-446655440001",
        name="Keyboard",
        description="Mechanical gaming keyboard",
        created_at="2026-07-13T20:00:00"
    )

    return Product(
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


def test_order_item_valid():

    product = create_product()

    item = OrderItem(
        id="29bb065c-64cf-4f3a-a3b6-426c174317ba",
        product=product,
        quantity=2,
        price=90000
    )


    assert item.price == 90000
    
    
def test_order_item_stock_failed():

    product = create_product()


    with pytest.raises(ValueError):

        OrderItem(
            id="29bb065c-64cf-4f3a-a3b6-426c174317ba",
            product=product,
            quantity=10,
            price=9000
        )


def test_order_without_items():

    with pytest.raises(ValueError):

        Order(
            id="dff581fd-6959-4d89-8400-ce5f4202c6ec",
            customer=None,
            items=[],
            total_price=0,
            status="pending"
        )

def test_payment_success_without_paid_at(order):

    with pytest.raises(ValueError):

        Payment(
            id="b7046045-b7b4-4afd-8944-7f46275eb4c8",
            order=order,
            method="qris",
            status=PaymentStatus.SUCCESS,
            amount=order.total_price,
            paid_at=None,
            created_at="2026-07-13T22:00:00"
        )