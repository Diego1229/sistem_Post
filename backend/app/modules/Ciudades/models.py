from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.database import Base


class ciudad(Base):
    __table__ = "ciudad"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    departamento = Column(String(50), nullable=False, unique=True)
    direccion = Column(Text, nullable=False, unique=True)
    activo = Column(Boolean, default=True, nullable=False)
    id_pais = Column(Integer, ForeignKey("pais.id"))
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    pais = relationship("pais", back_populates="ciudad")
