from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from backend.app.db.database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    last_name = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    document_number = Column(String(20), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    id_rol = Column(Integer, ForeignKey("Role.id"))
    rol = relationship("Role", back_populates="users")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow, nullable=False)
