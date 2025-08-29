from fastapi import APIRouter
from backend.app.models.Role.Rol_Schemas import RoleBase

router = APIRouter()


@router.get("/")
def root():
    return {"msg": "mi api del rol"}


@router.post("/api/rol")
def create_role(data_role: RoleBase):
    return {"msg": "Rol creado", "data": data_role}
