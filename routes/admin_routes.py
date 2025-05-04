from fastapi import APIRouter, HTTPException, Depends
from db import get_db
from auth import verify_token
from fastapi.security import OAuth2PasswordBearer
"""Securely manage admin access via JWT.

Allow admins to view event registrations.

Optionally manage the registrations, like deleting them."""

router = APIRouter()

# OAuth2PasswordBearer instance for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# View all event registrations (admin only)
@router.get("/admin/registrations")
async def view_registrations(token: str = Depends(oauth2_scheme)):
    # Verify token and get user info
    user_info = verify_token(token)
    
    if not user_info or user_info.get("role") != "admin":
        # If no user info or role is not 'admin', raise Unauthorized error
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Connect to the database and fetch event registrations
    db = get_db()
    registrations = db.event_registrations.find()  # Get all event registrations
    registrations_list = list(registrations)  # Convert cursor to list
    
    # Return the list of event registrations
    return {"registrations": registrations_list}

# Optional: Admin-specific route to delete an event registration (just as an example)
@router.delete("/admin/registrations/{registration_id}")
async def delete_registration(registration_id: str, token: str = Depends(oauth2_scheme)):
    # Verify token and get user info
    user_info = verify_token(token)
    
    if not user_info or user_info.get("role") != "admin":
        raise HTTPException(status_code=401, detail="Unauthorized")

    db = get_db()
    result = db.event_registrations.delete_one({"_id": registration_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Registration not found")
    
    return {"message": "Registration deleted successfully"}
