from pydantic_settings import (
    BaseSettings,
)  # instead of 'from pydantic import BaseSettings'


class Settings(BaseSettings):
    app_name: str = "Cognitive Distortion Checker"
    environment: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
