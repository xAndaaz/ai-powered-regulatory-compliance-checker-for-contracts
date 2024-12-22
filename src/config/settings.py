import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "AI Compliance Checker")
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "data/uploads")
    ALLOWED_FILE_TYPE: str = "application/pdf"

settings = Settings()
