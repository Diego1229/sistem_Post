
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class RoleCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50,
                      description="nombre del rol")
    description: str = Field(..., min_length=1,
                             max_length=50, description="descripcion")

    @validator('name')
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError(
                'El nombre no puede estar vacío o solo contener espacios en blanco')
        return v.strip().title()

    @validator('description')
    def validate_description(cls, v):
        if not v.strip():
            raise ValueError(
                'La descripción no puede estar vacía o solo contener espacios en blanco')
        return v.strip()


class RoleUpdate(BaseModel):
    name: Optional[str] = Field(
        None, min_length=1, max_length=50, description="Nombre del rol")
    description: Optional[str] = Field(
        None, min_length=1, max_length=500, description="Descripción del rol")
    is_active: Optional[bool] = Field(
        None, description="Estado de activación del rol")

    @validator('name')
    def validate_name(cls, v):
        if v is not None:
            if not v.strip():
                raise ValueError(
                    'El nombre no puede estar vacío o solo contener espacios en blanco')
            return v.strip().title()
        return v

    @validator('description')
    def validate_description(cls, v):
        if v is not None:
            if not v.strip():
                raise ValueError(
                    'La descripción no puede estar vacía o solo contener espacios en blanco')
            return v.strip()
        return v


class RoleResponse(BaseModel):
    id: int
    name: str
    description: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class RoleBasic(BaseModel):
    id: int
    name: str
    is_active: bool

    class Config:
        from_attributes = True
