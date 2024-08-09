from app.models.user import User
from app.models.expense import Expense
from app.models.category import Category
from app.database.singleton import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.utils.password_helpers import check_password
from app.utils.token import create_access_token, verify_access_token
from typing import Annotated
from pydantic import BaseModel

oauth = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/api/v1/auth"
)


class LoginForm(BaseModel):
    username: str
    password: str


@router.post("/login/")
def login_user(credentials: LoginForm, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == credentials.username).first()
    if user is None or not check_password(user.password, credentials.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user.id)
    return JSONResponse(content={"access_token": token, "type": "Bearer"}, status_code=200)


@router.get("/me", dependencies=[Depends(oauth)])
def get_user_info(authorization: Annotated[str | None, Header()], db: Session = Depends(get_db)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Not Authenticated")

    jwt_token = authorization[7:]
    user_id = verify_access_token(jwt_token)

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = {
        "id": user.id,
        "full_name": user.full_name,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at.isoformat(),
        "updated_at": user.updated_at.isoformat(),
        # Add other fields as necessary
    }

    return JSONResponse(content=user_data, status_code=200)
