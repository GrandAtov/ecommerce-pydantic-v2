from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.db.models.category import Category
from app.db.base import Base

from uuid import UUID

from sqlalchemy import select

# # Create

Base.metadata.create_all(
    engine
)

# session = SessionLocal()

# category = Category(
#     name="Keyboard",
#     description="Mechanical keyboard"
# )

# session.add(category)

# session.commit()

# session.refresh(category)

# print(category.id)

# # Read

# session = SessionLocal()

# result = session.execute(
#     select(Category)
# )

# categories = result.scalars().all()

# for category in categories:
#     print(
#         category.id,
#         category.name
#     )


# with SessionLocal() as session:

#     category = session.execute(
#         select(Category).where(
#             Category.id == UUID("aefa30ef-ab78-4f49-ad10-9c74ad92e2bf")
#         )
#     ).scalar_one()


#     category.name = "Gaming Keyboard"


#     session.commit()


#     print(category.name)

# session = SessionLocal()

# category_id = UUID("aefa30ef-ab78-4f49-ad10-9c74ad92e2bf")

# category = session.get(
#     Category,
#     category_id
# )

# session.delete(category)

# session.commit()

