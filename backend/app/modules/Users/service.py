from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .models import Rol, Usuario, UsuarioSede
from .schemas import (
    RolCreate, RolUpdate,
    UsuarioCreate, UsuarioUpdate,
    UsuarioSedeCreate, UsuarioSedeUpdate
)
from .crud import RolCrud, UsuarioCrud, UsuarioSedeCrud


# ------------------------------------------------------
# ROL SERVICE
# ------------------------------------------------------

class RolService:
    def __init__(self, db: Session):
        self.db = db
        self.crud = RolCrud(db)

    def get_rol(self, rol_id: int):
        rol = self.crud.get(rol_id)
        if not rol:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Rol con id {rol_id} no encontrado"
            )
        return rol

    def get_all_roles(self):
        return self.crud.get_all()

    def create_rol(self, rol_data: RolCreate):
        # Validación: no permitir roles duplicados por nombre
        existing = self.db.query(Rol).filter(Rol.nombre == rol_data.nombre).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un rol con ese nombre"
            )
        return self.crud.create(rol_data)

    def update_rol(self, rol_id: int, rol_data: RolUpdate):
        rol = self.get_rol(rol_id)
        return self.crud.update(rol, rol_data)

    def delete_rol(self, rol_id: int):
        rol = self.get_rol(rol_id)
        # No permitir eliminar el rol "Administrador"
        if rol.nombre.lower() == "administrador":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No se puede eliminar el rol Administrador"
            )
        self.crud.delete(rol)
        return {"message": "Rol eliminado correctamente"}


# ------------------------------------------------------
# USUARIO SERVICE
# ------------------------------------------------------

class UsuarioService:
    def __init__(self, db: Session):
        self.db = db
        self.crud = UsuarioCrud(db)

    def get_usuario(self, usuario_id: int):
        usuario = self.crud.get(usuario_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuario con id {usuario_id} no encontrado"
            )
        return usuario

    def get_all_usuarios(self):
        return self.crud.get_all()

    def create_usuario(self, usuario_data: UsuarioCreate):
        # Validar duplicado por correo o username
        existing = self.db.query(Usuario).filter((Usuario.email == usuario_data.email) | (Usuario.cedula == usuario_data.cedula)).first()

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo o la cédula ya están registrados."
            )
        return self.crud.create(usuario_data)

    def update_usuario(self, usuario_id: int, usuario_data: UsuarioUpdate):
        usuario = self.get_usuario(usuario_id)
        # Se puede editar el usuario administrador
        return self.crud.update(usuario, usuario_data)

    def delete_usuario(self, usuario_id: int):
        usuario = self.get_usuario(usuario_id)

        # --- Protección: no permitir eliminar el Administrador principal ---
        if usuario.rol and usuario.rol.nombre.lower() == "administrador" and usuario.id == 1:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="⚠️ No se puede eliminar el usuario administrador principal del sistema"
            )

        self.crud.delete(usuario)
        return {"message": "Usuario eliminado correctamente"}


# ------------------------------------------------------
# USUARIO-SEDE SERVICE
# ------------------------------------------------------

class UsuarioSedeService:
    def __init__(self, db: Session):
        self.db = db
        self.crud = UsuarioSedeCrud(db)

    def get_usuario_sede(self, id: int):
        record = self.crud.get(id)
        if not record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"UsuarioSede con id {id} no encontrado"
            )
        return record

    def get_all(self):
        return self.crud.get_all()

    def create_usuario_sede(self, data: UsuarioSedeCreate):
        # Validar duplicado usuario-sede
        existing = self.db.query(UsuarioSede).filter(
            UsuarioSede.usuario_id == data.usuario_id,
            UsuarioSede.sede_id == data.sede_id
        ).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe esta asignación usuario-sede"
            )
        return self.crud.create(data)

    def update_usuario_sede(self, id: int, data: UsuarioSedeUpdate):
        record = self.get_usuario_sede(id)
        return self.crud.update(record, data)

    def delete_usuario_sede(self, id: int):
        record = self.get_usuario_sede(id)
        self.crud.delete(record)
        return {"message": "UsuarioSede eliminado correctamente"}
