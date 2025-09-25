from fastapi import APIRouter
from app.modules.Role import Routers as RoleRouters
from app.modules.Usuario import Routers as UsuarioRouters

api_router = APIRouter()
api_router.include_router(RoleRouters.router, prefix="/rol", tags=["Rol"])
api_router.include_router(UsuarioRouters.router,
                          prefix="/usuario", tags=["Usuario"])
