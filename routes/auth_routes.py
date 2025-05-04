from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from models import UserCreate, UserLogin, Token
from auth import create_access_token, hash_password, verify_password, verify_token
from db import get_db
from typing import List

router = APIRouter()

# OAuth2PasswordBearer instance for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# User registration endpoint
@router.post("/register")
async def register(user: UserCreate):
    db = get_db()
    # Check if user already exists in the database
    existing_user = db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the user's password
    hashed_password = hash_password(user.password)
    
    # Store user details in MongoDB
    db.users.insert_one({"username": user.username, "email": user.email, "password": hashed_password})
    return {"message": "User registered successfully"}

# User login endpoint
@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    db = get_db()
    # Fetch user from the database
    stored_user = db.users.find_one({"email": user.email})
    
    if not stored_user or not verify_password(user.password, stored_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Generate access token after successful authentication
    access_token = create_access_token(data={"sub": stored_user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

# Function to get current user (for authenticated routes)
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        return verify_token(token)
    except HTTPException:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
