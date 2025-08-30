from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from backend.app.db.database import Base


class Role(Base):
    __tablename__ = "Role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow, nullable=False)
    users = relationship("User", back_populates="role")
