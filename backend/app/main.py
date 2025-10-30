from fastapi import FastAPI
from app import modules
from backend.app.db.scalar_config import setup_scalar

app = FastAPI()

# Configurar Scalar
setup_scalar(app)

# Registrar rutas
app.include_router()


@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API!"}
