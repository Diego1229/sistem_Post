from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.database import get_db
from .import Rol_Schemas, Service_Rol, Role_Crud


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

# --- Crear un nuevo rol ---


@router.post("/", response_model=Rol_Schemas.RoleResponse)
def create_role(role: Rol_Schemas.RoleCreate, db: Session = Depends(get_db)):
    return Service_Rol.create_role_service(db, role)


# --- Obtener todos los roles ---

@router.get("/", response_model=list[Rol_Schemas.RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return Service_Rol.get_roles_service(db)

# obtener rol por id


@router.get("/roles/{role_id}", response_model=Rol_Schemas.RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    return Service_Rol.get_role_service(db, role_id)


# Actualizar un rol


@router.put("/{role_id}", response_model=Rol_Schemas.RoleResponse)
def update_role(role_id: int, role: Rol_Schemas.RoleUpdate, db: Session = Depends(get_db)):
    db_role = Role_Crud.update_role(db, role_id, role)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role


# Eliminar un rol

@router.delete("/{role_id}", response_model=Rol_Schemas.RoleResponse)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    db_role = Role_Crud.delete_role(db, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role
