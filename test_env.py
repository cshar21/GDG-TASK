import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Test if the MONGO_URI variable is loaded
mongo_uri = os.getenv('MONGO_URI')

print(f"MONGO_URI: {mongo_uri}")  # Should print the URI if loaded correctly
