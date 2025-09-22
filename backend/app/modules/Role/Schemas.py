
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class rolcreate (BaseModel):
    nombre: str
    descripcion: Optional[str] = None


class rolupdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    activo: Optional[bool] = None


class rolresponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    activo: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime


class config:
    orm_mode = True
