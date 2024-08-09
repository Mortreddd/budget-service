from fastapi import APIRouter, Depends
from app.models.category import Category
from app.models.expense import Expense
from app.models.user import User
from app.database.singleton import get_db
from sqlalchemy.orm import Session, joinedload

router = APIRouter(
    prefix="/api/v1/categories"
)


@router.get(path="/")
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).options(joinedload(Category.expenses)).all()
    return categories


@router.get(path="/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = (db.query(Category)
                .where(Category.id == category_id)
                .options(joinedload(Category.expenses))
                .first())

    return {"category": category}
