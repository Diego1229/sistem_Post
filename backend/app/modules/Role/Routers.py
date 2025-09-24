from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from .import Crud, Schemas, Service

router = APIRouter()

# --- Crear un nuevo rol ---


@router.post("/", response_model=Schemas.rolresponse)
def crear_rol(rol: Schemas.rolcreate, db: Session = Depends(get_db)):
    return Service.crear_rol_service(db=db, rol=rol)


@router.get("/", response_model=list[Schemas.rolresponse])
def listar_rol(db: Session = Depends(get_db)):
    return Service.get_rol_service(db)


@router.get("/{id}", response_model=Schemas.rolresponse)
def list_rol_id(id: int, db: Session = Depends(get_db)):
    return Service.get_rol_id_service(db, id)


@router.put("/{id}", response_model=Schemas.rolupdate)
def update_rol(id: int, rol_update: Schemas.rolupdate, db: Session = Depends(get_db)):
    return Service.update_rol_service(db, id, rol_update)


@router.delete("/{id}",  response_model=Schemas.rolresponse)
def delete_rol(id: int, db: Session = Depends(get_db)):
    return Crud.delete_rol(db=db, id=id)
