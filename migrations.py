from app.models.category import Category
from app.models.user import User
from app.database.singleton import get_db
from app.utils.password_helpers import hash_password
from datetime import datetime
from typing import List
import logging

logging.basicConfig(level=logging.INFO)


def migrate_categories() -> None:
    db = next(get_db())
    try:
        if db.query(Category).count() > 0:
            logging.info("Categories already exist, skipping migration.")
            return

        categories: List[Category] = [
            Category(name="Groceries"),
            Category(name="Shopping"),
            Category(name="Fare"),
            Category(name="Food"),
            Category(name="Utilities"),
            Category(name="Others")
        ]
        db.add_all(categories)
        db.commit()
        logging.info("Categories migrated successfully.")
    except Exception as e:
        db.rollback()
        logging.error(f"Error migrating categories: {e}")
    finally:
        db.close()


def migrate_users() -> None:
    db = next(get_db())
    try:
        if db.query(User).count() > 0:
            logging.info("Users already exist, skipping migration.")
            return

        user: User = User(
            full_name="Emmanuel Male",
            username="Mortreddd",
            email="emmanmale@gmail.com",
            password=hash_password("emmanuelmale25"),
            created_at=datetime.now(),
        )

        db.add(user)
        db.commit()
        logging.info("User migrated successfully.")
    except Exception as e:
        db.rollback()
        logging.error(f"Error migrating user: {e}")
    finally:
        db.close()


def make_migrations() -> None:
    migrate_categories()
    migrate_users()


if __name__ == "__main__":
    make_migrations()
