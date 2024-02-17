from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_API_KEY: str = "6777180102:AAF1TyJw-PfVunfKiIlckiY6v911NV44mfQ"

    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa

settings = Settings()