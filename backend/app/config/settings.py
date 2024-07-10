import os

from app.utils.fileloader import FileLoader
from pydantic import BaseModel


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

    __fileloader = FileLoader()

    DIRPATHS = __fileloader.DIRPATHS
    FILEPATHS = __fileloader.FILEPATHS

    DB = DatabaseConfig(
        ID=os.getenv("DB_ID"),
        PROJECT_ID=os.getenv("APPWRITE_PROJECT_ID"),
        API_KEY=os.getenv("APPWRITE_API_KEY"),
        PATIENT_COLLECTION_ID=os.getenv("PATIENT_COLLECTION_ID"),
        DOCTOR_COLLECTION_ID=os.getenv("DOCTOR_COLLECTION_ID"),
        APPOINTMENT_COLLECTION_ID=os.getenv("APPOINTMENT_COLLECTION_ID"),
        BUCKET_ID=os.getenv("BUCKET_ID"),
    )


settings = Settings()
