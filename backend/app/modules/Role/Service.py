from sqlalchemy.orm import Session
from . import Crud, Models, Schemas
from fastapi import HTTPException, status

# Crear rol con validación


def crear_rol_service(db: Session, rol: Schemas.rolcreate):
    existente = db.query(Models.Rol).filter(
        Models.Rol.nombre == rol.nombre).count()
    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El rol '{rol.nombre}' ya existe"
        )
    return Crud.post_rol(db, rol)


# listar los roles

def get_rol_service(db: Session):
    roles = Crud.get_roles(db)
    if not roles:
        raise HTTPException(
            status_code=404,
            detail="No hay roles registrados"
        )
    return roles

# Obtener un rol por id


def get_rol_id_service(db: Session, id: int):
    rol = Crud.get_rol_id(db, id)
    if not rol:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    return rol


# Actualizar rol (usa tu función put_rol de crud)

def update_rol_service(db: Session, id: int, rol_update: Schemas.rolupdate):
    rol = Crud.put_rol(db, id, rol_update)
    return rol
