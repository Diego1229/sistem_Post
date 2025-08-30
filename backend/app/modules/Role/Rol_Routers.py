from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.database import get_db
from .import Rol_Schemas, Service_Rol, Role_Crud

router = APIRouter()

# --- Crear un nuevo rol ---


@router.post("/", response_model=Rol_Schemas.RoleResponse)
def crear_rol(role: Rol_Schemas.RoleCreate, db: Session = Depends(get_db)):
    return Service_Rol.create_role_service(db, role)


# --- Obtener todos los roles ---
@router.get("/", response_model=list[Rol_Schemas.RoleResponse])
def obtener_roles(db: Session = Depends(get_db)):
    return Service_Rol.get_roles_service(db)


# --- Obtener un rol por ID ---
@router.get("/{role_id}", response_model=Rol_Schemas.RoleResponse)
def obtener_rol(role_id: int, db: Session = Depends(get_db)):
    rol = Service_Rol.get_role_service(db, role_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol


# --- Actualizar un rol ---
@router.put("/{role_id}", response_model=Rol_Schemas.RoleResponse)
def actualizar_rol(role_id: int, role: Rol_Schemas.RoleUpdate, db: Session = Depends(get_db)):
    rol_actualizado = Service_Rol.Role_Crud.update_role(db, role_id, role)
    if not rol_actualizado:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol_actualizado


# --- Eliminar un rol ---
@router.delete("/{role_id}", response_model=Rol_Schemas.RoleResponse)
def eliminar_rol(role_id: int, db: Session = Depends(get_db)):
    rol_eliminado = Service_Rol.Role_Crud.delete_role(db, role_id)
    if not rol_eliminado:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol_eliminado
