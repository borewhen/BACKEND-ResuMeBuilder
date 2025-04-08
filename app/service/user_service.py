from datetime import timedelta, datetime
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from app.models.user import User  # Adjust import if necessary
from app.database import get_db
from sqlalchemy.orm import Session
import os
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, Depends, Request

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
print(SECRET_KEY)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, email: str, password: str) -> Optional[dict]:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None

    # Generate access token
    token_data = {"sub": str(user.user_id), "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
    access_token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {
        "access_token": access_token,
        "user": {
            "id": user.user_id,
            "name": user.username,
            "email": user.email,
            "role": user.role,
        }
    }


def hash_password(password):
    return pwd_context.hash(password)


def jwt_required(request: Request, db: Session = Depends(get_db)):
    """Extracts and verifies the current user from JWT token"""
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing Authorization token")

    token = auth_header.split(" ")[1]

    try:
        # Decode JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=403, detail="Invalid password or username")

        # Fetch user from DB
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            raise HTTPException(status_code=403, detail="Invalid password or username")

        return user

    except Exception:
        raise HTTPException(status_code=403, detail="Invalid password or username")
