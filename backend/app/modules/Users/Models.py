from sqlalchemy import Column, Integer, String,Text , Boolean, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from ...db.database import Base

class Rol(Base):
    __tablename__ = "rol"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    descripcion = Column(Text, nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow,
                                 onupdate=datetime.utcnow, nullable=False)
    usuarios = relationship("Usuario", back_populates="rol")


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(50), nullable=True, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    telefono = Column(Integer, nullable=False, unique=True)
    activo = Column(Boolean, default=True, nullable=False)
    rol_id = Column(Integer, ForeignKey("rol.id"), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    rol = relationship("Rol", back_populates="usuarios")
#   sedes = relationship("UsuarioSede", back_populates="usuario")


class UsuarioSede(Base):
    __tablename__ = "usuario_sede"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
#   sede_id = Column(Integer, ForeignKey("sedes.id"), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    usuario = relationship("Usuario", back_populates="sedes")
#   sede = relationship("Sede", back_populates="usuarios_sede")