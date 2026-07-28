from app.db.session import SessionLocal, engine
from app.db.models import Category

from sqlalchemy import select

session = SessionLocal()

# Step 1
results = session.execute(
    select(Category)
).scalars().all()

for result in results:
    print(f"id={result.id}, name='{result.name}', description='{result.description}'")
    
    
# Step 2
result2 = session.execute(
    select(Category)
    .where(Category.name == "Keyboard")
).first()

result2_att = result2[0] 

print(f"id={result2_att.id}, name='{result2_att.name}', description='{result2_att.description}'")

# Step 3
result3 = session.execute(
    select(Category)
    .where(Category.name == "Laptop ASUS")
).first()

print(result3)
# Muncul hasil None

# Step 4.1
result4_1 = session.execute(
    select(Category)
    .where(Category.name == "Laptop")
).one()

print(result4_1)
# Hasil ada

# Step 4.2
result4_2 = session.execute(
    select(Category)
    .where(Category.name == "Mouse")
).one()

print(result4_2)
# Hasil error

# Step 5.1
result5_1 = session.execute(
    select(Category)
    .where(Category.name == "Keyboard")
).one_or_none()

print(result5_1)
# Hasil Ada

# Step 5.2
result5_2 = session.execute(
    select(Category)
    .where(Category.name == "Laptop ASUS")
).one_or_none()

print(result5_2)
# Hasil None

# Step 6
result6 = session.execute(
    select(Category)
    .where(Category.name == "Keyboard")
).one()

print(result6)
# Perbedaannya adalah apa yang dikembalikan one() adalah seperti Tuple atau row baris sedangkan scalar_one() adalah versi unpack nya

# Step 7
result7 = session.execute(
    select(Category)
    .where(Category.name == "Keyboard", Category.is_active == True, Category.description == "Perangkat keras masukan (input device) pada komputer atau laptop yang berisi susunan tombol huruf, angka, simbol, dan fungsi khusus. Alat ini berfungsi untuk mengetik teks, memasukkan data, dan memberikan perintah ke dalam sistem perangkat elektronik.")
).scalar_one()

print(result7)

# Step 8 
result8 = session.execute(
    select(Category)
    .where(Category.is_active == True, Category.name == "Keyboard")
).scalar_one()

print(result8)


# Step 9_1
result9_1 = session.execute(
    select(Category)
    .order_by(Category.name)
).scalars().all()

print(result9_1)

# Step 9_2
result9_2 = session.execute(
    select(Category)
    .order_by(Category.name.desc())
).scalars().all()

print(result9_2)


# Step 10
result10 = session.execute(
    select(Category)
    .limit(2)
).scalars().all()

print(result10)

# Step 11
result11 = session.execute(
    select(Category)
    .offset(1)
    .limit(2)
).scalars().all()

print(result11)

