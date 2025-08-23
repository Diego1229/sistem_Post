from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database import Base


class Role(Base):
    _tablename_ = "Roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow, nullable=False)
    user = relationship("User", back_populates="rol")


class User(Base):
    _tablename_ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    last_name = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    document_number = Column(String(20), nullable=False, unique=True)
    phone = Column(String(20), nullable=False, unique=True)
    is_active = Column(Boolean, default=True, nullable=False)
    id_rol = Column(Integer, ForeignKey("roles.id"))
    rol = relationship("Role", back_populates="User")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow, nullable=False)
