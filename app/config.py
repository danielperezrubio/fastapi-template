from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    TITLE: str = "FastAPI"
    BACKEND_CORS_ORIGINS: str = ""


settings = Settings()
