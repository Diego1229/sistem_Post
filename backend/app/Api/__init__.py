from fastapi import APIRouter
from backend.app.modules.Role import Rol_Routers

api_router = APIRouter()
api_router.include_router(Rol_Routers.router, prefix="/roles", tags=["Roles"])
