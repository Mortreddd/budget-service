from .config import SessionLocal
from sqlalchemy.orm import DeclarativeBase


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
