from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.app.core.config import settings

# Crear el motor de la base de datos MySQL
engine = create_engine(
    settings.database_url,
    echo=settings.debug,  # Mostrar queries SQL en desarrollo
    pool_pre_ping=True,   # Verificar conexiones antes de usarlas
    pool_recycle=300      # Reciclar conexiones cada 5 minutos
)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la DB


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
