from fastapi import APIRouter
from app.schemas.Rol_Schemas import RoleBase

router = APIRouter()


@router.get("/")
def root():
    return {"msg": "mi api del rol"}


@router.post("/")
def create_role(data_role: RoleBase):
    return {"msg": "Rol creado", "data": data_role}
