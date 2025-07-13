from datetime import datetime, timezone
from typing import Dict, Any
from sqlalchemy import Column, Integer, String, DateTime
from .base import Base


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)  # Changed from phone_number to phone
    email = Column(String(100), nullable=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    def __repr__(self):
        return f"<Hospital(id={self.id}, name={self.name}, address={self.address})>"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the hospital instance to a dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


__all__ = ["Hospital"]
