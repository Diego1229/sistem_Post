from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from . import crud, Schemas, service

router = APIRouter()


@router.post("/", response_model=Schemas.UsuarioResponse)
def crear_usuario(usuario: Schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return service.crear_usuario_service(db=db, Usuario=usuario)  # aqui


@router.get("/", response_model=list[Schemas.UsuarioResponse])
def listar_usuario(db: Session = Depends(get_db)):
    return service.get_usuario_service(db)


@router.get("/{id}", response_model=Schemas.UsuarioResponse)
def list_usuario_id(id: int, db: Session = Depends(get_db)):
    return service.get_usuario_id_service(db, id)


@router.put("/{id}", response_model=Schemas.UsuarioUpdate)
def update_usuario(id: int, usuario_update: Schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    return service.update_usuario_service(db, id, usuario_update)


@router.delete("/{id}", response_model=Schemas.UsuarioResponse)
def delete_usuario(id: int, db: Session = Depends(get_db)):
    return crud.delete_usuario(db=db, id=id)
