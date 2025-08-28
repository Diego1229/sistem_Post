from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RoleBase(BaseModel):
    name: str
    description: str
    is_active: bool


class RoleCreate(RoleBase):
    pass


class RoleResponse(RoleBase):
    id: int
    create_at: datetime
    update_at: datetime

    class config:
        orm_mode = True
