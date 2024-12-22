import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Default App")
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "False").lower() == "true"
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "data/uploads")
    ALLOWED_FILE_TYPES: list = os.getenv("ALLOWED_FILE_TYPES", "pdf").split(",")

settings = Settings()
