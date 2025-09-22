from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from ...db.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    apellido = Column(String(50), nullable=False)
    contrasena = Column(String(255), nullable=False)
    correo = Column(String(250), nullable=False, unique=True)
    numero_documento = Column(String(20), nullable=False, unique=True)
    telefono = Column(String(20), nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    id_rol = Column(Integer, ForeignKey("rol.id"))
    rol = relationship("Rol", back_populates="usuarios")
    creado_en = Column(DateTime, default=datetime.utcnow)
    actualizado_en = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
