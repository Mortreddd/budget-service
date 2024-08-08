from fastapi import APIRouter, Depends
from ..models.category import Category
from ..models.expense import Expense
from ..models.user import User
from ..database.singleton import get_db
from sqlalchemy.orm import Session, joinedload
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/v1/categories/{category_id}/expenses"
)


@router.get("/")
def get_expenses(category_id: int, db: Session = Depends(get_db)):
    expenses = (db.query(Expense)
                .where(Expense.category_id == category_id)
                .all())
    db.close()
    return expenses


class CreateExpense(BaseModel):
    user_id: int
    amount: float


@router.post("/create/")
def create_expense(category_id: int, expense: CreateExpense, db: Session = Depends(get_db)):
    new_expense = Expense(
        category_id=category_id,
        user_id=expense.user_id,
        amount=expense.amount
    )
    try:
        db.add(new_expense)
        db.commit()
    except Exception as e:
        db.rollback()
        return {"status": 422, "message": e}
    finally:
        db.close()

    return new_expense

