from sqlalchemy import Column, Integer, String,Text , Boolean, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from ...db.database import Base



class Pais(Base):
    __tablename__ = "paises"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre= Column(String(50), nullable=True, unique=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    ciudades = relationship("ciudad", back_populates="pais")


class Ciudad(Base):
    __tablename__ = "ciudades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    departamento = Column(String(50), nullable=False)
    pais_id = Column(Integer, ForeignKey("paises.id"), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    pais = relationship("Pais", back_populates="ciudades")
    sedes = relationship("Sede", back_populates="ciudad")
    

class Sede(Base):
    __tablename__ = "sede"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    direccion = Column(String(200))
    telefono = Column(String(50), nullable=False, unique=True)
    activo = Column(Boolean, default=True, nullable=False)
    ciudad_id = Column(Integer, ForeignKey("ciudades.id"), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    ciudad = relationship("Ciudad", back_populates="sedes")
    usuarios_sede = relationship("UsuarioSede", back_populates="sede")

