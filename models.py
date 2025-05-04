from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# User creation model
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# User login model
class UserLogin(BaseModel):
    username: str
    password: str

# User model (general use)
class User(BaseModel):
    username: str
    email: str
    password: str

# Token response
class Token(BaseModel):
    access_token: str
    token_type: str

# Event creation model
class Event(BaseModel):
    title: str
    description: str
    location: str
    date: datetime
    time: datetime

# Event registration model
class EventRegistration(BaseModel):
    event_id: str
    user_email: str

# QR Code response model
class QRCode(BaseModel):
    user_email: str
    event_id: str
    qr_code: str
