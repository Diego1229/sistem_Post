import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


class Settings:
    # Base de datos MySQL (sin contraseña)
    database_url: str = os.getenv(
        "DATABASE_URL", "mysql+pymysql://root@localhost:3306/sistem_post_db")
    mysql_host: str = os.getenv("MYSQL_HOST", "localhost")
    mysql_port: int = int(os.getenv("MYSQL_PORT", "3306"))
    mysql_user: str = os.getenv("MYSQL_USER", "root")
    mysql_password: str = os.getenv("MYSQL_PASSWORD", "")
    mysql_database: str = os.getenv("MYSQL_DATABASE", "sistem_post_db")

    # Seguridad
    secret_key: str = os.getenv(
        "SECRET_KEY", "tu-clave-secreta-super-segura-aqui")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # Servidor
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    debug: bool = os.getenv("DEBUG", "True").lower() == "true"

    # Configuración del proyecto
    project_name: str = "Sistema de Posts"
    version: str = "1.0.0"
    description: str = "API para sistema de posts con FastAPI"


# Instancia global de configuración
settings = Settings()
