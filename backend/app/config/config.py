from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Cargar variables de entorno
load_dotenv()


class Settings(BaseSettings):
    app_name: str
    debug: bool
    secret_key: str
    database_url: str
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()