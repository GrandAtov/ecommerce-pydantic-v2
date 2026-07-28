from app.db.session import SessionLocal
from app.db.models.category import Category


session = SessionLocal()

category1 = Category(
    name="Tablet",
    description="Perangkat seperti handphone yang berukuran lebih besar hampir seukuran layar laptop",
    is_active=True
)
session.add(category1)

session.commit()

session.refresh(category1)

category2 = session.get(Category, category1.id)

print(category2)

session.delete(category2)

session.commit()

deleted_category = session.get(Category, category1.id)

print(deleted_category)



