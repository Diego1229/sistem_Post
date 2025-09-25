from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# class UserBase(BaseModel): # Esquema base que comparten create/response
# name: str
# last_name: str
# email: EmailStr
# phone: str
# document_number:str


class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    contrasena: str
    correo: EmailStr
    numero_documento: str
    telefono: Optional[str] = None
    id_rol: int


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    contrasena: Optional[str] = None
    correo: Optional[EmailStr] = None
    numero_documento: Optional[str] = None
    telefono: Optional[str] = None
    activo: Optional[bool] = None
    id_rol: Optional[int] = None


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo: EmailStr
    numero_documento: str
    telefono: Optional[str]
    activo: bool
    id_rol: int
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        orm_mode = True
