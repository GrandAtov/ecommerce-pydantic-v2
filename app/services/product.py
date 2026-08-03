from uuid import UUID

from app.services.base import BaseService

from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository

from app.db.models.product import Product

from app.schemas.product import (
    ProductCreate,
    ProductUpdate
)

class ProductService(BaseService[ProductRepository]):
    def __init__(self, category_repository: CategoryRepository, product_repository: ProductRepository):
        super().__init__(product_repository)
        
        self.category_repository = category_repository
        
    def create_product(self, data: ProductCreate) -> Product:
        existing_category = self.category_repository.get_by_id(data.category_id)
        
        if existing_category is None:
            raise ValueError("Category tidak ditemukan")
        
        return self.repository.create(
            Product(
                name=data.name,
                brand=data.brand,
                description=data.description,
                price=data.price,
                discount=data.discount,
                stock = data.stock,
                image_url = data.image_url,
                category_id = data.category_id
            )
        )
        
    def search(self, keyword: str) -> list[Product]:
        return self.repository.search(keyword)
    
    def get_latest(self) -> list[Product]:
        return self.repository.get_latest()
    
    def get_product(self, product_id: UUID) -> Product:
        product = self.repository.get_by_id(product_id)
        
        if product is None:
            raise ValueError("Produk tidak ditemukan")
        
        return product
