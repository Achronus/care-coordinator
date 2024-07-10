import os

from app.config.env import load_dotenv_file
from pydantic import BaseModel


load_dotenv_file(".env.local", "care_coordinator")


class DatabaseConfig(BaseModel):
    """A place to store the appwrite database settings."""

    ID: str
    PROJECT_ID: str
    API_KEY: str
    PATIENT_COLLECTION_ID: str
    DOCTOR_COLLECTION_ID: str
    APPOINTMENT_COLLECTION_ID: str
    BUCKET_ID: str


class Settings:
    """A model for storing all config settings."""

    DB = DatabaseConfig(
        ID=str(os.getenv("DB_ID")),
        PROJECT_ID=str(os.getenv("APPWRITE_PROJECT_ID")),
        API_KEY=str(os.getenv("APPWRITE_API_KEY")),
        PATIENT_COLLECTION_ID=str(os.getenv("PATIENT_COLLECTION_ID")),
        DOCTOR_COLLECTION_ID=str(os.getenv("DOCTOR_COLLECTION_ID")),
        APPOINTMENT_COLLECTION_ID=str(os.getenv("APPOINTMENT_COLLECTION_ID")),
        BUCKET_ID=str(os.getenv("BUCKET_ID")),
    )


settings = Settings()
