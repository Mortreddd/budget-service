from ..database.singleton import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .expense import Expense


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    expenses = relationship("Expense", back_populates="category")
