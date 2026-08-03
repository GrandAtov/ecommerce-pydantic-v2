from uuid import UUID

from app.repositories.category_repository import CategoryRepository

from app.db.models.category import Category

from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate
)

from app.services.base import BaseService

class CategoryService(BaseService[CategoryRepository]):
    def __init__(self, category_repository: CategoryRepository):
        super().__init__(category_repository)
        
    def create_category(self, data: CategoryCreate) -> Category:
        existing_category = self.repository.find_by_name(data.name)
        
        if existing_category:
            raise ValueError("Kategori sudah ada")
        
        return self.repository.create(
            Category(
                name=data.name,
                description=data.description,
                is_active=data.is_active,
            )
        )
        
    def get_active_categories(self) -> list[Category]:
        return self.repository.get_active_categories()
        
    def get_category(self, category_id: UUID) -> Category:
        category = self.repository.get_by_id(category_id)
        
        if category is None:       
            raise ValueError("Kategori tidak ditemukan")
        
        return category