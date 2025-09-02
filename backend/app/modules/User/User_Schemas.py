from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel): # Esquema base que comparten create/response
    name: str
    last_name: str
    email: EmailStr
    phone: str
    document_number:str


class UserCreate(UserBase): # Datos que llegan al crear usuario
    password:str
    id_rol: int

