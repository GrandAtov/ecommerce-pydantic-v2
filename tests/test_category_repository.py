# tests/repositories/test_category_repository.py
from decimal import Decimal
import pytest

from app.db.models.category import Category
from app.db.models.order import Order
from app.db.models.order_item import OrderItem
from app.repositories.category_repository import CategoryRepository


class TestCategoryRepository:
    """Test untuk Category Repository"""
    
    def test_create_category(self, session):
        """Test membuat category baru"""
        repo = CategoryRepository(session)
        
        category = Category(
            name="Keyboard",
            description="Mechanical Keyboard"
        )
        
        result = repo.create(category)
        
        assert result.id is not None
        assert result.name == "Keyboard"
        assert result.description == "Mechanical Keyboard"
        assert result.is_active is True  # Default value
    
    def test_find_by_name(self, session):
        """Test mencari category berdasarkan nama"""
        repo = CategoryRepository(session)
        
        # Create category
        category = Category(
            name="Monitor",
            description="Gaming Monitor"
        )
        repo.create(category)
        
        # Find by name
        found = repo.find_by_name("Monitor")
        
        assert found is not None
        assert found.name == "Monitor"
        assert found.description == "Gaming Monitor"
    
    def test_get_active_categories(self, session):
        """Test mendapatkan category yang aktif"""
        repo = CategoryRepository(session)
        
        # Create categories
        active_cat = Category(
            name="Laptop",
            description="Gaming Laptop",
            is_active=True
        )
        inactive_cat = Category(
            name="Tablet",
            description="Android Tablet",
            is_active=False
        )
        
        repo.create(active_cat)
        repo.create(inactive_cat)
        
        # Get active categories
        active_categories = repo.get_active_categories()
        
        assert len(active_categories) == 1
        assert active_categories[0].name == "Laptop"
        assert active_categories[0].is_active is True


class TestProductWithCategory:
    """Test untuk relasi Product dan Category"""
    
    def test_get_product_with_category(self, session, product):
        """Test product memiliki category yang valid"""
        # product fixture sudah memiliki category_id
        assert product.category_id is not None
        assert product.category is not None
        assert product.category.name == "Keyboard"
        assert product.category.description == "Mechanical Keyboard"
    
    def test_product_category_relationship(self, session, product):
        """Test relasi antara product dan category"""
        # Product bisa mengakses category melalui relationship
        category = product.category
        
        assert category is not None
        assert category.id == product.category_id
        assert category.name == "Keyboard"
        
        # Category juga bisa mengakses products
        assert len(category.products) >= 1
        assert product in category.products


class TestOrderWithItems:
    """Test untuk Order dan OrderItem"""
    
    def test_create_order_with_items(self, session, customer, product):
        """Test membuat order dengan order items"""
        # Buat order
        order = Order(
            customer_id=customer.id,
            total_price=Decimal("1000000")
        )
        session.add(order)
        session.commit()
        session.refresh(order)
        
        # Buat order item
        item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=2,
            price=Decimal("900000")
        )
        session.add(item)
        session.commit()
        session.refresh(item)
        
        # Assertions
        assert item.order_id == order.id
        assert item.product_id == product.id
        assert item.quantity == 2
        assert item.price == Decimal("900000")
        
        # Relasi dari order ke order_items
        assert len(order.order_items) == 1
        assert order.order_items[0].id == item.id
        assert order.order_items[0].product_id == product.id
    
    def test_order_has_customer(self, session, customer):
        """Test relasi order dengan customer"""
        order = Order(
            customer_id=customer.id,
            total_price=Decimal("500000")
        )
        session.add(order)
        session.commit()
        session.refresh(order)
        
        # Order bisa mengakses customer
        assert order.customer is not None
        assert order.customer.id == customer.id
        assert order.customer.name == "Grand"
        
        # Customer bisa mengakses orders
        assert len(customer.orders) >= 1
        assert order in customer.orders


class TestIntegration:
    """Test integrasi antar model"""
    
    def test_complete_order_flow(self, session, customer, product, category):
        """Test alur lengkap pembuatan order"""
        # 1. Buat category (sebenarnya sudah dari fixture)
        assert category.name == "Keyboard"
        
        # 2. Buat product (sebenarnya sudah dari fixture)
        assert product.name == "Keyboard RGB"
        assert product.category_id == category.id
        
        # 3. Buat order
        order = Order(
            customer_id=customer.id,
            total_price=Decimal("2000000")
        )
        session.add(order)
        session.commit()
        session.refresh(order)
        
        # 4. Buat order item
        item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=3,
            price=Decimal("650000")  # Harga setelah diskon
        )
        session.add(item)
        session.commit()
        session.refresh(item)
        
        # 5. Verifikasi semua relasi
        # Order → Customer
        assert order.customer.name == "Grand"
        
        # Order → OrderItems → Product
        assert len(order.order_items) == 1
        assert order.order_items[0].product.name == "Keyboard RGB"
        assert order.order_items[0].product.category.name == "Keyboard"
        
        # Customer → Orders
        assert len(customer.orders) >= 1
        assert customer.orders[0].id == order.id
        
        # Product → OrderItems → Order
        assert len(product.order_items) >= 1
        assert product.order_items[0].order_id == order.id