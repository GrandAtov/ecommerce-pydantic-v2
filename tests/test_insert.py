from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.db.models import Category
    
session = SessionLocal()

category = Category(
    name="Handphone",
    description="Handphone adalah alat komunikasi elektronik genggam yang berfungsi untuk melakukan panggilan, mengirim pesan, serta menjelajah internet.",
    is_active=True
)

session.add(category)

session.commit()

session.refresh(category)

print(category)

session.close()

