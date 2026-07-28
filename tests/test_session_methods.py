from uuid import UUID

from app.db.session import SessionLocal
from app.db.models.category import Category

# Step 1
session = SessionLocal()

category1 = Category(
    name="Monitor",
    description="Perangkat keras keluaran (output) yang berfungsi untuk menampilkan data visual seperti teks, gambar, dan video dari hasil pemrosesan komputer. Perangkat ini juga dikenal sebagai Video Display Terminal (VDT).",
    is_active=True
)

session.add(category1)

print(category1.id)

session.flush()

print(category1.id)

session.rollback()

print()
# Step 2
category2 = Category(
    name="Speaker",
    description="Perangkat keras keluaran yang berfungsi mengubah sinyal listrik menjadi gelombang suara, dengan komponen utama seperti membran, kumparan, dan magnet.",
    is_active=True
)

session.add(category2)

session.commit()

print(category2.created_at)

session.refresh(category2)

print(category2.created_at)

# Step 3
category3 = session.get(Category, UUID("5bd7c54174304df5b25873bedb694845"))

category3.name = "Ponsel"

session.rollback()

session.refresh(category3)

print(category3.name)

# Step 4
category4 = session.get(Category, UUID("5bd7c54174304df5b25873bedb694845"))

print(category4.name)

session.expire(category4)

print(category4.name)

