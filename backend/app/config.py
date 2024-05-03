import os

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Rozetka Scraper API"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    PROJECT_VERSION: str = "1.0.0"
    ECHO_SQL: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

