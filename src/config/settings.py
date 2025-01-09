import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "AI Compliance Checker")
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "data/uploads")
    ALLOWED_FILE_TYPE: str = "application/pdf"
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT: str = os.getenv("PINECONE_ENVIRONMENT")
    PINECONE_INDEX_NAME: str = os.getenv("PINECONE_INDEX_NAME", "ai-compliance-embeddings")


settings = Settings()