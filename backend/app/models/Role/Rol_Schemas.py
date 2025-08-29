from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RoleBase(BaseModel):
    name: str
    description: str
    is_active: bool = True  # Valor por defecto


class RoleCreate(RoleBase):
    pass


class RoleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class RoleResponse(RoleBase):
    id: int
    created_at: datetime  # Corregido: era create_at
    updated_at: datetime  # Corregido: era update_at

    class Config:  # Corregido: era config
        from_attributes = True  # Nuevo en Pydantic v2, antes era orm_mode = True
