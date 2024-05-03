import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Rozetka Scraper API"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    PROJECT_VERSION: str = "1.0.0"
    ECHO_SQL: bool = True

    class Config:
        env_file = "backend/app/.env"
        case_sensitive = True


settings = Settings()
