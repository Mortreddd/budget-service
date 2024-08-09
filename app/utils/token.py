from datetime import datetime, timedelta
from fastapi.exceptions import HTTPException
import jwt
from dotenv import load_dotenv
import os

load_dotenv()


EXPIRATION_TIME = datetime.utcnow() + timedelta(days=2)
ALGORITHM: str = "HS256"
SECRET_KEY: str = os.getenv("SECRET_KEY")


def create_access_token(user_id: int) -> str:
    payload = {
        "sub": user_id,
        "exp": EXPIRATION_TIME.isoformat(),
        "iat": datetime.utcnow().isoformat()
    }

    encoded_jwt = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return encoded_jwt


# params: jwt_token : string
# returns user id of the user
def verify_access_token(jwt_token: str) -> int:
    payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=403, detail="Forbidden")

    return user_id
