from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    AWS_SERVER_PUBLIC_KEY: str
    AWS_SERVER_SECRET_KEY: str
    AWS_REGION: str
    ENDPOINT: str
    PORT: str
    DB_USER: str
    PASSWORD: str
    DBNAME: str
    REGION: str

    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8") # noqa


settings = Settings()
