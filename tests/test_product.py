import pytest

from pydantic import ValidationError

from app.models import Product



def test_product_success(product):

    assert product.name == "Keyboard RGB"

    assert product.discount == 10



def test_product_price_negative(category):

    with pytest.raises(ValidationError):

        Product(
            id="550e8400-e29b-41d4-a716-446655440010",
            name="Keyboard RGB",
            brand="Logitech",
            description="Mechanical keyboard gaming",
            price=-100,
            discount=10,
            stock=10,
            image_url="https://example.com/image.jpg",
            category=category,
            created_at="2026-07-13T21:00:00"
        )



def test_product_discount_invalid(category):

    with pytest.raises(ValidationError):

        Product(
            id="550e8400-e29b-41d4-a716-446655440010",
            name="Keyboard RGB",
            brand="Logitech",
            description="Mechanical keyboard gaming",
            price=100000,
            discount=120,
            stock=10,
            image_url="https://example.com/image.jpg",
            category=category,
            created_at="2026-07-13T21:00:00"
        )



def test_product_auto_generate_sku(category):

    product = Product(
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


    assert product.sku == "PROD-KEY-LOG-MEC"