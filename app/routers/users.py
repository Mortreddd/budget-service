from fastapi import APIRouter, Depends
from ..models.category import Category
from ..models.expense import Expense
from ..models.user import User
from ..database.singleton import get_db
from sqlalchemy.orm import Session, joinedload

router = APIRouter(
    prefix="/api/v1/users"
)


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).options(joinedload(User.expenses))
    return {"status": 200, "data": users}


@router.post("/create/")
def create_user(user: User, db: Session = Depends(get_db)):
    try:
        db.add(user)
        db.commit()
    except Exception as e:
        db.rollback()
        return {"status": 422, "message": e}
    finally:
        db.close()

    return {"status": 201,
            "message": "Expense created",
            "data": user
            }
