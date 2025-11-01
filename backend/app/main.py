from fastapi import FastAPI
from app.modules.Users import users_router
from app.db.scalar_config import setup_scalar

app = FastAPI(title="API General")

setup_scalar(app)

# Incluir rutas del módulo Users
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API!"}

