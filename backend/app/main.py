from fastapi import FastAPI
from app.Api import api_router
from app import modules
from backend.app.config.scalar_config import setup_scalar

app = FastAPI()

# Configurar Scalar
setup_scalar(app)

# Registrar rutas
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API!"}
