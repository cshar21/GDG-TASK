import os
import pymongo
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

"""# Load environment variables from the .env file (for secure credential management)
load_dotenv()

# Fetch MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")

print("Loaded MONGO_URI:", os.getenv("MONGO_URI"))
print(f"MONGO_URI is: {os.getenv('MONGO_URI')}")

if not MONGO_URI:
    raise ValueError("❌ MONGO_URI is not set in the .env file")

MONGO_URI = "mongodb+srv://chakshusharma21s:E7iE8Kky7AExcdSP@qrcluster.qmchv13.mongodb.net/?retryWrites=true&w=majority"

# Database name (can be adjusted if needed)
DATABASE_NAME = "qr_event_checkin"  # Update with your actual database name

def get_db() -> pymongo.database.Database:
    # Function to connect to MongoDB and get the database.
try:
        # Initialize the MongoDB client with the connection URI
        client = pymongo.MongoClient(MONGO_URI)
        
        # Return the database by name
        db = client[DATABASE_NAME]
        
        # Verify the connection by pinging the server
        client.admin.command('ping')  # This will raise an exception if the connection fails
        print(f"✅ Successfully connected to the database: {db.name}")
        return db
    except ConnectionFailure as e:
        print(f"❌ Could not connect to MongoDB: {e}")
        raise
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")
        raise

# Helper function to get a specific collection from the database
def get_collection(collection_name: str):
    # Get a collection from the database.
    db = get_db()
    return db[collection_name]

# Example Usage: Test connecting to the database and collections
def example_usage():
    # Example: Get the events collection
    events_collection = get_collection("events")  # Replace with your actual collection name
    users_collection = get_collection("users")  # Replace with your actual collection name
    
    # Example: Insert a sample event document into the "events" collection
    event = {
        "title": "Sample Event",
        "date": "2025-05-01",
        "location": "Event Hall A",
    }
    events_collection.insert_one(event)

    # Example: Fetch all events
    events = list(events_collection.find())
    print("All events:", events)

    # Example: Fetch a specific user
    user_email = "student@example.com"
    user = users_collection.find_one({"email": user_email})
    print("Fetched user:", user)

if __name__ == "__main__":
    # Call example_usage to test if connection works
    example_usage()
"""

# db.py (MOCK VERSION for screenshots)

print("⚠️ Using MOCK database — no real MongoDB connection.")

# Fake in-memory collections
class FakeCollection:
    def insert_one(self, data):
        print("🟢 insert_one called with:", data)
        return {"inserted_id": "mock_id_123"}

    def find_one(self, query):
        print("🔍 find_one called with:", query)
        return {"_id": "mock_id_123", "username": "testuser", "role": "student"}

    def find(self, query={}):
        print("🔎 find called with:", query)
        return [
            {"_id": "mock_id_123", "username": "testuser", "role": "student"},
            {"_id": "mock_id_124", "username": "admin", "role": "admin"},
        ]

    def update_one(self, query, update):
        print("🛠 update_one called with:", query, update)
        return {"modified_count": 1}

# Mock database
class MockDB:
    def __init__(self):
        self._collections = {
            "users": FakeCollection(),
            "events": FakeCollection(),
            "registrations": FakeCollection(),
        }

    def __getitem__(self, name):
        return self._collections.get(name, FakeCollection())

    def command(self, cmd):
        print(f"🧪 Mock command called with: {cmd}")
        return {"ok": 1}

def get_db():
    print("⚠️ Returning MOCK database.")
    return MockDB()