from backend.app.core.database import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("conexion exitosa", result.scalar())
except Exception as e:
    print("error al conectar")
