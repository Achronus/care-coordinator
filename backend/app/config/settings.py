from app.config.env import load_dotenv_file
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv_file(".env.demo", "care_coordinator")


class DatabaseConfig(BaseModel):
    """A place to store the appwrite database settings."""

    ID: str | None = None
    PROJECT_ID: str | None = None
    API_KEY: str | None = None
    PATIENT_COLLECTION_ID: str | None = None
    DOCTOR_COLLECTION_ID: str | None = None
    APPOINTMENT_COLLECTION_ID: str | None = None
    BUCKET_ID: str | None = None
    ENDPOINT_URL: str | None = None


class Settings(BaseSettings):
    """A model for storing all config settings."""

    DB: DatabaseConfig

    model_config = SettingsConfigDict(
        env_file=".env.backend", env_nested_delimiter="__"
    )


settings = Settings()
