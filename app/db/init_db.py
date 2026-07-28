from app.db.base import Base
from app.db.session import engine
from app.db.models import (
    Address,
    Category,
    Customer,
    OrderItem,
    Order,
    Payment,
    Product
)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully.")
    print(engine.url)
    
if __name__ == "__main__":
    init_db()