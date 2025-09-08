from fastapi import APIRouter, Depends, HTTPException
from models import UserCreate, UserResponse
from database import users_collection
from utils import hash_password, verify_password, create_access_token
from datetime import datetime
from models import UserCreate, UserResponse

router = APIRouter()

"""
POST /auth/register - Register user
POST /auth/login - Login with JWT
"""

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    hashed_password = hash_password(user.password)
    user.password = hashed_password

@router.post("/login", response_model=UserResponse)
async def login_user(user: UserCreate):
    user = await users_collection.find_one({"email": user.email})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(user.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(user.model_dump())
    return {"access_token": access_token, "token_type": "bearer"}