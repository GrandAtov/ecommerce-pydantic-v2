# tests/repositories/test_relationships.py
import pytest
from decimal import Decimal
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

from app.db.models.category import Category
from app.db.models.product import Product
from app.db.models.customer import Customer
from app.db.models.address import Address
from app.db.models.order import Order, OrderStatus
from app.db.models.order_item import OrderItem
from app.db.models.payment import Payment


class TestCategoryRelationships:
    """Test relasi Category dengan model lain"""
    
    def test_category_has_products(self, session, category, product):
        """Test Category dapat mengakses Products"""
        session.refresh(category)
        
        assert len(category.products) >= 1
        assert category.products[0].id == product.id
        assert category.products[0].name == "Keyboard RGB"
        assert category.products[0].category_id == category.id
        
    def test_category_products_relationship(self, session):
        """Test relasi one-to-many Category → Products"""
        category = Category(
            name="Electronics",
            description="Electronic devices"
        )
        session.add(category)
        session.commit()
        session.refresh(category)
        
        product1 = Product(
            name="Laptop",
            brand="Dell",
            description="Gaming Laptop",
            sku="LAP001",
            price=Decimal("15000000"),
            discount=Decimal("5"),
            stock=10,
            image_url="https://example.com/laptop.jpg",
            category_id=category.id
        )
        product2 = Product(
            name="Mouse",
            brand="Logitech",
            description="Wireless Mouse",
            sku="MOU001",
            price=Decimal("500000"),
            discount=Decimal("0"),
            stock=20,
            image_url="https://example.com/mouse.jpg",
            category_id=category.id
        )
        
        session.add_all([product1, product2])
        session.commit()
        session.refresh(category)
        
        assert len(category.products) == 2
        product_names = [p.name for p in category.products]
        assert "Laptop" in product_names
        assert "Mouse" in product_names


class TestCustomerRelationships:
    """Test relasi Customer dengan model lain"""
    
    def test_customer_has_orders(self, session, customer, order):
        """Test Customer dapat mengakses Orders"""
        session.refresh(customer)
        
        assert len(customer.orders) >= 1
        assert customer.orders[0].id == order.id
        assert customer.orders[0].customer_id == customer.id
        
    def test_customer_has_addresses(self, session, customer, address):
        """Test Customer dapat mengakses Addresses"""
        session.refresh(customer)
        
        assert len(customer.addresses) >= 1
        assert customer.addresses[0].id == address.id
        assert customer.addresses[0].customer_id == customer.id
        
    def test_customer_multiple_addresses(self, session, customer):
        """Test Customer dengan multiple addresses"""
        # 🔥 MASALAH: Address dari fixture hilang karena session berbeda?
        # Solusi: Buat ulang semua address di test ini
        
        # Hapus semua address yang ada (jika ada)
        session.refresh(customer)
        for addr in customer.addresses:
            session.delete(addr)
        session.commit()
        session.refresh(customer)
        
        # Buat address baru dari awal
        address1 = Address(
            name="Rumah",
            street="Jl. Merdeka No. 1",
            city="Pontianak",
            province="Kalbar",
            postal_code="78111",
            country="Indonesia",
            customer_id=customer.id
        )
        address2 = Address(
            name="Kantor",
            street="Jl. Sudirman No. 1",
            city="Jakarta",
            province="DKI Jakarta",
            postal_code="10110",
            country="Indonesia",
            customer_id=customer.id
        )
        address3 = Address(
            name="Rumah Baru",
            street="Jl. Kebon Jeruk No. 10",
            city="Jakarta",
            province="DKI Jakarta",
            postal_code="10220",
            country="Indonesia",
            customer_id=customer.id
        )
        
        session.add_all([address1, address2, address3])
        session.commit()
        session.refresh(customer)
        
        # Assert: Customer memiliki 3 addresses
        assert len(customer.addresses) == 3
        
        # Verifikasi nama addresses
        address_names = [a.name for a in customer.addresses]
        assert "Rumah" in address_names
        assert "Kantor" in address_names
        assert "Rumah Baru" in address_names
        
    def test_customer_orders_relationship(self, session, customer):
        """Test relasi Customer → Orders (one-to-many)"""
        session.refresh(customer)
        
        # 🔥 Hapus semua order yang ada (jika ada)
        for ord in customer.orders:
            session.delete(ord)
        session.commit()
        session.refresh(customer)
        
        # Buat 3 order baru
        order1 = Order(
            customer_id=customer.id,
            total_price=Decimal("1000000"),
            status=OrderStatus.PENDING
        )
        order2 = Order(
            customer_id=customer.id,
            total_price=Decimal("2000000"),
            status=OrderStatus.PAID
        )
        order3 = Order(
            customer_id=customer.id,
            total_price=Decimal("1500000"),
            status=OrderStatus.SHIPPED
        )
        
        session.add_all([order1, order2, order3])
        session.commit()
        session.refresh(customer)
        
        # Assert: Customer memiliki 3 orders
        assert len(customer.orders) == 3
        
        # Verifikasi total prices
        total_prices = [o.total_price for o in customer.orders]
        assert Decimal("1000000") in total_prices
        assert Decimal("2000000") in total_prices
        assert Decimal("1500000") in total_prices


class TestOrderRelationships:
    """Test relasi Order dengan model lain"""
    
    def test_order_has_customer(self, session, order, customer):
        """Test Order dapat mengakses Customer"""
        session.refresh(order)
        
        assert order.customer is not None
        assert order.customer.id == customer.id
        assert order.customer.name == "Grand"
        
    def test_order_has_order_items(self, session, order, order_item):
        """Test Order dapat mengakses OrderItems"""
        session.refresh(order)
        
        assert len(order.order_items) >= 1
        assert order.order_items[0].id == order_item.id
        assert order.order_items[0].order_id == order.id
        
    def test_order_has_payment(self, session, order, payment):
        """Test Order dapat mengakses Payment"""
        session.refresh(order)
        
        assert order.payment is not None
        assert order.payment.id == payment.id
        assert order.payment.order_id == order.id
        
    def test_order_multiple_order_items(self, session, order, product, customer):
        """Test Order dengan multiple OrderItems"""
        # 🔥 MASALAH: Order items dari fixture hilang
        # Solusi: Hapus semua order items, buat ulang
        
        session.refresh(order)
        
        # Hapus semua order items yang ada
        for item in order.order_items:
            session.delete(item)
        session.commit()
        session.refresh(order)
        
        # Buat product tambahan
        product1 = Product(
            name="Keyboard RGB",
            brand="Logitech",
            description="Gaming Keyboard",
            sku="KB001",
            price=Decimal("1000000"),
            discount=Decimal("10"),
            stock=10,
            image_url="https://example.com/image.jpg",
            category_id=product.category_id
        )
        product2 = Product(
            name="Monitor",
            brand="Samsung",
            description="Monitor 24 inch",
            sku="MON001",
            price=Decimal("3000000"),
            discount=Decimal("5"),
            stock=5,
            image_url="https://example.com/monitor.jpg",
            category_id=product.category_id
        )
        
        session.add_all([product1, product2])
        session.commit()
        session.refresh(product1)
        session.refresh(product2)
        
        # Buat order items
        order_item1 = OrderItem(
            order_id=order.id,
            product_id=product1.id,
            quantity=2,
            price=Decimal("900000")
        )
        order_item2 = OrderItem(
            order_id=order.id,
            product_id=product2.id,
            quantity=1,
            price=Decimal("2850000")
        )
        
        session.add_all([order_item1, order_item2])
        session.commit()
        session.refresh(order)
        
        # Assert: Order memiliki 2 order items
        assert len(order.order_items) == 2
        
        # Verifikasi product names
        product_names = [item.product.name for item in order.order_items]
        assert "Keyboard RGB" in product_names
        assert "Monitor" in product_names


class TestCascadeDelete:
    """Test cascade delete relationships"""
    
    def test_delete_order_cascades_to_order_items(self, session, order, order_item):
        """Test menghapus Order akan menghapus OrderItems"""
        order_id = order.id
        order_item_id = order_item.id
        
        session.delete(order)
        session.commit()
        
        deleted_order = session.get(Order, order_id)
        deleted_item = session.get(OrderItem, order_item_id)
        
        assert deleted_order is None
        assert deleted_item is None
        
    def test_delete_product_does_not_delete_order_items(self, session, product, order_item):
        """Test menghapus Product TIDAK menghapus OrderItems"""
        # 🔥 Gunakan IntegrityError
        session.refresh(product)
        assert len(product.order_items) > 0, "Product harus punya order_items"
        
        with pytest.raises(IntegrityError) as exc_info:
            session.delete(product)
            session.commit()
        
        assert exc_info.type is IntegrityError
        
        session.rollback()
        
        # Verifikasi product masih ada
        product_exists = session.get(Product, product.id)
        assert product_exists is not None


# 🔥 TEST BARU: Test dengan data custom
class TestCustomScenarios:
    """Test skenario kustom"""
    
    def test_customer_without_addresses(self, session, clean_customer):
        """Test customer tanpa address"""
        session.refresh(clean_customer)
        
        # Customer dari clean_customer tidak punya address
        assert len(clean_customer.addresses) == 0
        
    def test_customer_without_orders(self, session, clean_customer):
        """Test customer tanpa orders"""
        session.refresh(clean_customer)
        
        # Customer dari clean_customer tidak punya orders
        assert len(clean_customer.orders) == 0
        
    def test_delete_customer_without_relations(self, session, clean_customer):
        """Test delete customer tanpa relasi"""
        customer_id = clean_customer.id
        
        # Customer tidak punya relasi, bisa dihapus
        session.delete(clean_customer)
        session.commit()
        
        deleted_customer = session.get(Customer, customer_id)
        assert deleted_customer is None