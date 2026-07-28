from app.db.session import SessionLocal
from app.db.models.category import Category

from sqlalchemy import select

session = SessionLocal()

category1 = session.execute(
    select(Category)
    .where(Category.name == "Keyboard Gaming")
).scalar_one()

category1.name = "Keyboard RGB"
category1.description = "Papan tik dengan lampu latar Red, Green, Blue yang menawarkan kustomisasi jutaan warna, estetika modern, dan visibilitas di tempat gelap."

session.commit()

session.refresh(category1)

print(category1)
