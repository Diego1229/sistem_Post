from sqlalchemy.orm import Session
from . import Role_Crud, Rol_Schemas, Rol_Models
from fastapi import HTTPException, status


# Crear un rol con validación de duplicado
def create_role_service(db: Session, role: Rol_Schemas.RoleCreate):
    try:
        return Role_Crud.create_rol(db, role)
    except Exception as e:
        if "UNIQUE constraint failed" in str(e) or "duplicate key" in str(e):
            raise HTTPException(
                status_code=400, detail="El nombre del rol ya existe")
        raise HTTPException(
            status_code=500, detail="Error interno del servidor")


# Obtiene todos los roles registrados en la base de datos.

def get_roles_service(db: Session):
    roles = Role_Crud.get_roles(db)
    if not roles:
        return []
    return roles


#  Obtiene un rol específico por su ID.

def get_role_service(db: Session, role_id: int):
    if role_id <= 0:
        raise HTTPException(
            status_code=422,
            detail="El ID del rol debe ser un número positivo"
        )

    role = Role_Crud.get_role(db, role_id)
    if not role:
        raise HTTPException(
            status_code=404,
            detail="Rol no encontrado"
        )
    return role

# 📌 Actualiza un rol existente en la base de datos.


def update_role_service(db: Session, role_id: int, role: Rol_Schemas.RoleUpdate):
    if role_id <= 0:
        raise HTTPException(
            status_code=422, detail="El ID del rol debe ser un número positivo")

    # Validar que al menos un campo se envíe para actualizar
    if not any(getattr(role, field) is not None for field in role.dict(exclude_unset=True)):
        raise HTTPException(
            status_code=422, detail="Debe proporcionar al menos un campo para actualizar")

    try:
        db_role = Role_Crud.update_role(db, role_id, role)
        if not db_role:
            raise HTTPException(status_code=404, detail="Rol no encontrado")
        return db_role
    except Exception as e:
        if "UNIQUE constraint failed" in str(e) or "duplicate key" in str(e):
            raise HTTPException(
                status_code=400, detail="El nombre del rol ya existe")
        raise HTTPException(
            status_code=500, detail="Error interno del servidor")


# Eliminar un rol

def delete_role_service(db: Session, role_id: int):
    if role_id <= 0:
        raise HTTPException(
            status_code=422, detail="El ID del rol debe ser un número positivo")

    # Verificar que el rol exista antes de eliminar
    existing_role = Role_Crud.get_role(db, role_id)
    if not existing_role:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
