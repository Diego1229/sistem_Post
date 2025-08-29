from fastapi import FastAPI
from backend.app.models.Role.Rol_Routers import router as Rol_Routers

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Bienvenido a mi API 🚀"}


app.include_router(Rol_Routers, prefix="/roles", tags=["roles"])
