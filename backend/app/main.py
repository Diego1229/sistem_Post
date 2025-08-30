from fastapi import FastAPI
from backend.app.Api import api_router
from backend.app import modules

app = FastAPI()

app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API!"}
