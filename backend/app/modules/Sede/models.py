# from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text
# from datetime import datetime
# from sqlalchemy.orm import relationship
# from app.db.database import Base


# class sedes(Base):
#     __table__ = "sedes"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     nombre = Column(String(50), nullable=False, unique=True)
#     telefono = Column(Integer, nullable=False, unique=True)
#     activo = Column(Boolean, default=True, nullable=False)
#     id_ciudad = Column(Integer, ForeignKey("ciudad.id"))
#     fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
#     fecha_actualizacion = Column(
#         DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
#     ciudad = relationship("Ciudad", back_populates="sedes")
