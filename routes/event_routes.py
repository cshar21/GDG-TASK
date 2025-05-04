from fastapi import APIRouter, HTTPException, Depends
from models import Event, EventRegistration
from db import get_db
from auth import verify_token
from fastapi.security import OAuth2PasswordBearer
from utils.qr_generator import generate_qr_code  # Import the QR code generation utility
from utils.email_sender import send_email  # Import email sending function
"""
Event Creation: Admins (or authorized users) should be able to create events.

Event Listing: Users should be able to list all available events.

Event Registration: Users should be able to register for an event.

Security: We'll use JWT authentication to make sure only authorized users (admins, in particular) can create events, while users can register or view events.
"""

router = APIRouter()
# OAuth2PasswordBearer instance for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Create Event (admin only)
@router.post("/admin/events")
async def create_event(event: Event, token: str = Depends(oauth2_scheme)):
    # Verify token and check if the user has admin privileges
    user_info = verify_token(token)
    if not user_info or user_info.get("role") != "admin":
        raise HTTPException(status_code=401, detail="Unauthorized")

    db = get_db()
    # Insert the event into the database
    db.events.insert_one(event.dict())  # Save event to database
    return {"message": "Event created successfully"}

# Get All Events (public route)
@router.get("/events")
async def get_events():
    db = get_db()
    events = db.events.find()  # Get all events from the database
    return {"events": list(events)}

# Register User for Event (authenticated users)
@router.post("/events/{event_id}/register")
async def register_for_event(event_id: str, token: str = Depends(oauth2_scheme)):
    # Verify token and check user authentication
    user_info = verify_token(token)
    if not user_info:
        raise HTTPException(status_code=401, detail="Unauthorized")

    db = get_db()
    # Check if the event exists
    event = db.events.find_one({"_id": event_id})
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Check if the user is already registered
    existing_registration = db.event_registrations.find_one({"event_id": event_id, "user_email": user_info["email"]})
    if existing_registration:
        raise HTTPException(status_code=400, detail="Already registered for this event")

    # Create the registration document
    registration = EventRegistration(event_id=event_id, user_email=user_info["email"])
    db.event_registrations.insert_one(registration.dict())

    # Generate QR code for registration
    qr_code = generate_qr_code(user_info["email"], event_id)
    
    # Send confirmation email with QR code to the user
    send_email(user_info["email"], f"Registration Confirmation for Event: {event['title']}", 
               f"Thank you for registering for the event. Here is your QR Code: {qr_code}")

    return {"message": "Successfully registered for the event", "qr_code": qr_code}

# Admin Route: View Registrations for a Specific Event (admin only)
@router.get("/admin/events/{event_id}/registrations")
async def get_event_registrations(event_id: str, token: str = Depends(oauth2_scheme)):
    # Verify token and check if the user has admin privileges
    user_info = verify_token(token)
    if not user_info or user_info.get("role") != "admin":
        raise HTTPException(status_code=401, detail="Unauthorized")

    db = get_db()
    
     # Get all registrations for the event
    registrations = db.event_registrations.find({"event_id": event_id})
    return {"registrations": list(registrations)}