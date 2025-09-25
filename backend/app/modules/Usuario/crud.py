from sqlalchemy.orm import Session
from . import Models, Schemas
from fastapi import HTTPException


def crear_usuario(db: Session, usuario: Schemas.UsuarioCreate):
    db_usuario = Models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def get_Usuario(db: Session):
    return db.query(Models.Usuario).all()


def get_Usuario_id(db: Session, id: int):
    return db.query(Models.Usuario). filter(Models.Usuario.id == id).first()


def put_Usuario(db: Session, id: int, Usuario_Update: Schemas.UsuarioUpdate):
    usuario = db.query(Models.Usuario).filter(Models.Usuario.id == id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    datos_update = Usuario_Update.dict(exclude_unset=True)
    for key, value in datos_update.items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario


def delete_usuario(db: Session, id: int):
    usuario = db.query(Models.Usuario).filter(Models.Usuario.id == id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.activo = False  # type: ignore
    db.commit()
    db.refresh(usuario)
    return {"mensaje": f"Usuario {usuario.id} desactivado correctamente"}
