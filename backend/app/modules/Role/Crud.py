from sqlalchemy.orm import Session
from . import Models, Schemas
from fastapi import HTTPException

# Crear rol con validación


def post_rol(db: Session, rol: Schemas.rolcreate):
    db_rol = Models.Rol(**rol.dict())
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

# listar los roles


def get_roles(db: Session):
    return db.query(Models).all()

# Obtener un rol por id


def get_rol_id(db: Session, id: int):
    return db.query(Models.Rol).filter(Models.Rol.id == id).first()

# Actualizar rol (usa tu función put_rol de crud)


def put_rol(db: Session, id: int, rol_update: Schemas.rolupdate):
    rol = db.query(Models.Rol).filter(Models.Rol.id == id).first()
    if rol is None:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    datos_update = rol_update.dict(exclude_unset=True)
    for key, value in datos_update.items():
        setattr(rol, key, value)
    db.commit()
    db.refresh(rol)
    return rol


def delete_rol(db: Session, id: int):
    rol = db.query(Models.Rol).filter(Models.Rol.id == id).first()
    if rol is None:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    rol.activo = False  # type: ignore
    db.commit()
    db.refresh(rol)
    return {"mensaje": f"Rol {rol.id} desactivado correctamente"}
