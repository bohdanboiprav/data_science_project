from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_API_KEY: str

    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa: F841

settings = Settings()