from pydantic import BaseModel, EmailStr, Field, constr, SecretStr
from typing import Optional
from datetime import datetime

class RolBase(BaseModel):
    nombre: constr(min_length=1, max_length=50)
    descripcion: Optional[str] = None
    activo: Optional[bool] = True

class RolCreate(RolBase):
    pass

class RolUpdate(BaseModel):
    nombre: Optional[constr(min_length=1, max_length=50)] = None
    descripcion: Optional[str] = None
    activo: Optional[bool] = None

class RolResponse(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    activo: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True

#----------------------------------------------------------------------------------

class UsuarioBase(BaseModel): 
    nombre: str
    cedula: int
    email: EmailStr
    telefono: Optional[str] = None
    activo: Optional[bool] = True


class UsuarioCreate(UsuarioBase):
    password: SecretStr
    rol_id: int

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    cedula: Optional[int] = None
    email: Optional[EmailStr] = None
    telefono: Optional[int] = None
    password: Optional[SecretStr] = None
    activo: Optional[bool] = None
    rol_id: Optional[int] = None

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    cedula: int
    email: EmailStr
    telefono: Optional[str] = None
    activo: bool
    rol_id: int
    Fecha_creacion: datetime
    Fecha_actualizacion: datetime

    class Config:
        orm_mode = True


#-------------------------------------------------------------------------------------------

class UsuarioSedeBase(BaseModel):
    usuario_id: int
    sede_id: int

class UsuarioSedeCreate(UsuarioSedeBase):
    pass

class UsuarioSedeUpdate(BaseModel):
    usuario_id: Optional[int] = None
    sede_id: Optional[int] = None

class UsuarioSedeResponse(BaseModel):
    id: int
    usuario_id: int
    sede_id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
    