from app.repositories.base import BaseRepository
from app.db.models.category import Category

def test_create_category(session):
    repo = BaseRepository(session, Category)

    category = Category(
        name="Keyboard",
        description="Mechanical Keyboard"
    )

    result = repo.create(category)

    assert result.id is not None
    assert result.name == "Keyboard"