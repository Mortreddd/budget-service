from app.database.singleton import Base
from app.database.config import engine
from app.models.category import Category
from app.models.expense import Expense
from app.models.user import User

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)