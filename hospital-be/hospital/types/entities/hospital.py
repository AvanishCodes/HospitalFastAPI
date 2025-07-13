from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timezone


@dataclass
class Hospital:
    id: int
    name: str
    address: str
    phone: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)

    def __post_init__(self):
        if not self.name:
            raise ValueError("Hospital name cannot be empty")
        if not self.address:
            raise ValueError("Hospital address cannot be empty")

    @property
    def to_dict(self) -> dict[str, str | int | None]:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


__all__ = [
    "Hospital",
]
