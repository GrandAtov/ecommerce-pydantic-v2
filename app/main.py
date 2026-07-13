from .models.category import Category
from .models.product import Product

category = Category(
    id="550e8400-e29b-41d4-a716-446655440001",
    name="Keyboard",
    description="Mechanical gaming keyboard",
    created_at="2026-07-13T20:00:00"
)

product = Product(
    id="550e8400-e29b-41d4-a716-446655440010",
    name="Mechanical Keyboard RGB",
    description="Mechanical keyboard with RGB backlight and hot-swappable switches.",
    price=899000,
    stock=15,
    image_url="https://example.com/images/keyboard.jpg",
    created_at="2026-07-13T21:00:00",
    category=category
)
