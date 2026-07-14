from app.models import Category, Product, Address, Customer, OrderItem, Order, Payment


category1 = Category(
    id="550e8400-e29b-41d4-a716-446655440001",
    name="Keyboard",
    description="Mechanical gaming keyboard",
    created_at="2026-07-13T20:00:00"
)

category2 = Category(
    id="1e9c3ead-30fc-4a75-a47a-53036d3e7b5e",
    name="Mouse",
    description="Gaming mouse",
    created_at="2026-07-13T21:00:00"
)

product1 = Product(
    id="550e8400-e29b-41d4-a716-446655440010",
    name="Mechanical Keyboard RGB",
    description="Mechanical keyboard with RGB backlight and hot-swappable switches.",
    price=899000,
    stock=15,
    image_url="https://example.com/images/keyboard.jpg",
    created_at="2026-07-13T21:00:00",
    category=category1
)

product2 = Product(
    id="37c393e7-5bc9-46c8-8463-d99a2195fb30",
    name="Mouse Gaming",
    description="Mouse Gaming with RGB backlight.",
    price=1899000,
    stock=5,
    image_url="https://example.com/images/mouse.jpg",
    created_at="2026-07-13T22:00:00",
    category=category2
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

order_item1 = OrderItem(
    id="29bb065c-64cf-4f3a-a3b6-426c174317ba",
    product=product1,
    quantity=2,
    price=899000
)

order_item2 = OrderItem(
    id="777f9df7-e49b-45c3-bad1-b02d8660f049",
    product=product2,
    quantity=1,
    price=1899000
)

order = Order(
    id="dff581fd-6959-4d89-8400-ce5f4202c6ec",
    customer=customer,
    items=[
        order_item1,
        order_item2
    ],
    status="paid"
)

payment = Payment(
    id="b7046045-b7b4-4afd-8944-7f46275eb4c8",
    order=order,
    method="qris",
    status="success",
    amount=3697000,
    paid_at="2026-07-13T22:00:00",
    created_at="2026-07-13T22:00:00"
)
