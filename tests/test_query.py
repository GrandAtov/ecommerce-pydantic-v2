from uuid import UUID
from app.db.session import SessionLocal
from app.db.models.category import Category

from sqlalchemy import select, func

session = SessionLocal()

print("1. Ambil semua kategori aktif.")
result1 = session.execute(
    select(Category)
    .where(Category.is_active == True)
).scalars().all()

for result in result1:
    print(result, "\n")

print("2. Ambil kategori berdasarkan UUID.")

result2 = session.execute(
    select(Category)
    .where(Category.id == UUID("44026269179942a0ad8af57e0c28613f"))
).scalar_one_or_none()

print(result2, "\n")

print("3. Ambil 3 kategori pertama berdasarkan nama ASC.")

result3 = session.execute(
    select(Category)
    .order_by(Category.name)
    .limit(3)
).scalars().all()

for result in result3:
    print(result, "\n")
    
print("4. Ambil 3 kategori terakhir berdasarkan nama DESC.")
result4 = session.execute(
    select(Category)
    .order_by(Category.name.desc())
    .limit(3)
).scalars().all()

for result in result4:
    print(result, "\n")
    
print("5. Cari kategori yang mengandung kata 'Laptop' (menggunakan LIKE).")
result5 = session.execute(
    select(Category)
    .where(Category.name.ilike("%Laptop%"))
).scalars().all()

for result in result5:
    print(result, "\n")

print("6. Hitung jumlah seluruh kategori.")
result6 = session.execute(
    select(func.count()).select_from(Category)
).scalar_one()



print(result6)

session.close()