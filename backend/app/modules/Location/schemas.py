from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaisBase(BaseModel):
    nombre: str

class PaisCreate(PaisBase):
    pass

class PaisUpdate(BaseModel):
    nombre: Optional[str] = None

class PaisResponse(BaseModel):
    id: int
    nombre: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True

#----------------------------------------------------------------------------------

class CiudadBase(BaseModel): 
    nombre: str
    departamento: str


class CiudadCreate(CiudadBase):
    pais_id: int


class CiudadUpdate(BaseModel):
    nombre: Optional[str] = None
    departamento: Optional[str] = None
    id_pais: Optional[str] = None

class CiudadResponse(BaseModel):
    id: int
    nombre: str
    departamento: str
    pai_id: int
    Fecha_creacion: datetime
    Fecha_actualizacion: datetime

    class Config:
        orm_mode = True


#-------------------------------------------------------------------------------------------

class SedeBase(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    activo: bool

class SedeCreate(SedeBase):
    ciudad_id: int

class SedeUpdate(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    id_pais: Optional[int] = None
    activo: Optional[bool] = None
    ciudad_id: Optional[int] = None

class SedeResponse(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    id_pais: int
    activo: bool
    ciudad_id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
    