from sqlalchemy.orm import Session
from . import crud, Models, Schemas
from fastapi import HTTPException, status


def crear_usuario_service(db: Session, Usuario: Schemas.UsuarioCreate):
    existente = db.query(Models.Usuario).filter(
        Models.Usuario.nombre == Usuario.nombre).count()
    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El usuario '{Usuario.nombre}' ya existe"
        )
    return crud.crear_usuario(db, Usuario)


def get_usuario_service(db: Session):
    Usuario = crud.get_Usuario(db)
    if not Usuario:
        raise HTTPException(
            status_code=404,
            detail="No hay usuario registrados"
        )
    return Usuario


def get_usuario_id_service(db: Session, id: int):
    Usuario = crud.get_Usuario_id(db, id)
    if not Usuario:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    return Usuario


def update_usuario_service(db: Session, id: int, Usuario_update: Schemas.UsuarioUpdate):
    Usuario = crud.put_Usuario(db, id, Usuario_update)
    return Usuario
