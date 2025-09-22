from fastapi import APIRouter
from app.modules.Role import Routers

api_router = APIRouter()
api_router.include_router(Routers.router, prefix="/rol", tags=["Rol"])
