from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.service.user_service import authenticate_user  # Import the auth function
from app.database import get_db
from app.service import user_service
from jose import jwt, JWTError

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = user_service.hash_password(user.password)
    user.password = hashed_password
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(response: Response, user_credentials: UserLogin, db: Session = Depends(get_db)):
    user_data = authenticate_user(db, user_credentials.email, user_credentials.password)

    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Set HTTP-only cookie for access token
    response.set_cookie(
        key="access_token",
        value=user_data["access_token"],
        httponly=True,
        secure=False,  # Set to False if running locally without HTTPS
        samesite="Strict",
        max_age=60 * 60,  # 1 hour
    )

    return {"message": "Login successful", "user": user_data["user"]}