from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Cargar variables del archivo .env
load_dotenv()

class Settings(BaseSettings):
    app_name: str
    debug: bool
    environment: str
    secret_key: str
    access_token_expire_minutes: int
    database_url: str
    items_per_user: int
    default_language: str
    timezone: str

    # Configuración adicional de Pydantic
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()

# Instancia única reutilizable
settings = get_settings()
