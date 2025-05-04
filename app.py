from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.event_routes import router as event_router
from routes.admin_routes import router as admin_router
from db import get_db
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Setup MongoDB connection

get_db().command("ping")
print("✅ MongoDB Atlas connected successfully")

# check for connection
try:
    get_db().command("ping")
    print("✅ MongoDB Atlas connected successfully")
except Exception as e:
    print("❌ MongoDB connection failed:", e)


# Include the routes for different parts of the application
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(event_router, prefix="/event", tags=["event"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the QR Event Check-in System"}


try:
    get_db().command("ping")
    print("✅ MongoDB Atlas connected successfully")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
