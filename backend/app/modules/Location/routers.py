from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ...db.database import get_db
from .schemas import (
    RolCreate, RolUpdate, RolResponse,
    UsuarioCreate, UsuarioUpdate, UsuarioResponse,
    UsuarioSedeCreate, UsuarioSedeUpdate, UsuarioSedeResponse
)
from .service import RolService, UsuarioService, UsuarioSedeService

router = APIRouter(prefix="/api")

# ==========================================================
# ------------------------- ROLES ---------------------------
# ==========================================================
@router.get("/roles", response_model=list[RolResponse], tags=["Rol"])
def list_roles(db: Session = Depends(get_db)):
    service = RolService(db)
    return service.get_all_roles()


@router.get("/roles/{rol_id}", response_model=RolResponse, tags=["Rol"])
def get_rol(rol_id: int, db: Session = Depends(get_db)):
    service = RolService(db)
    return service.get_rol(rol_id)


@router.post("/roles", response_model=RolResponse, status_code=status.HTTP_201_CREATED, tags=["Rol"])
def create_rol(rol: RolCreate, db: Session = Depends(get_db)):
    service = RolService(db)
    return service.create_rol(rol)


@router.put("/roles/{rol_id}", response_model=RolResponse, tags=["Rol"])
def update_rol(rol_id: int, rol: RolUpdate, db: Session = Depends(get_db)):
    service = RolService(db)
    return service.update_rol(rol_id, rol)


@router.delete("/roles/{rol_id}", tags=["Rol"])
def delete_rol(rol_id: int, db: Session = Depends(get_db)):
    service = RolService(db)
    return service.delete_rol(rol_id)


# ==========================================================
# ------------------------ USUARIOS -------------------------
# ==========================================================
@router.get("/usuarios", response_model=list[UsuarioResponse], tags=["Usuario"])
def list_usuarios(db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.get_all_usuarios()


@router.get("/usuarios/{usuario_id}", response_model=UsuarioResponse, tags=["Usuario"])
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.get_usuario(usuario_id)


@router.post("/usuarios", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED, tags=["Usuario"])
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.create_usuario(usuario)


@router.put("/usuarios/{usuario_id}", response_model=UsuarioResponse, tags=["Usuario"])
def update_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.update_usuario(usuario_id, usuario)


@router.delete("/usuarios/{usuario_id}", tags=["Usuario"])
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.delete_usuario(usuario_id)


# ==========================================================
# ---------------------- USUARIO SEDE -----------------------
# ==========================================================
@router.get("/usuario-sede", response_model=list[UsuarioSedeResponse], tags=["UsuarioSede"])
def list_usuario_sede(db: Session = Depends(get_db)):
    service = UsuarioSedeService(db)
    return service.get_all()


@router.get("/usuario-sede/{id}", response_model=UsuarioSedeResponse, tags=["UsuarioSede"])
def get_usuario_sede(id: int, db: Session = Depends(get_db)):
    service = UsuarioSedeService(db)
    return service.get_usuario_sede(id)


@router.post("/usuario-sede", response_model=UsuarioSedeResponse, status_code=status.HTTP_201_CREATED, tags=["UsuarioSede"])
def create_usuario_sede(data: UsuarioSedeCreate, db: Session = Depends(get_db)):
    service = UsuarioSedeService(db)
    return service.create_usuario_sede(data)


@router.put("/usuario-sede/{id}", response_model=UsuarioSedeResponse, tags=["UsuarioSede"])
def update_usuario_sede(id: int, data: UsuarioSedeUpdate, db: Session = Depends(get_db)):
    service = UsuarioSedeService(db)
    return service.update_usuario_sede(id, data)


@router.delete("/usuario-sede/{id}", tags=["UsuarioSede"])
def delete_usuario_sede(id: int, db: Session = Depends(get_db)):
    service = UsuarioSedeService(db)
    return service.delete_usuario_sede(id)
