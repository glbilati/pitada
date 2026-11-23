from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://pitada:pitada@localhost:5432/pitada"
    session_secret: str = "dev-only-change-me"


@lru_cache
def get_settings() -> Settings:
    return Settings()
