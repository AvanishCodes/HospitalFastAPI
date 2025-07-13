from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateHospitalRequest:
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

    @property
    def to_dict(self) -> dict[str, str | None]:
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data: dict[str, str | None]) -> "CreateHospitalRequest":
        assert data["name"], "Name is required"
        return cls(
            name=data["name"],
            address=data.get("address"),
            phone=data.get("phone"),
            email=data.get("email"),
        )


@dataclass
class UpdateHospitalRequest:
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

    @property
    def to_dict(self) -> dict[str, str | None]:
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data: dict[str, str | None]) -> "UpdateHospitalRequest":
        return cls(
            name=data.get("name"),
            address=data.get("address"),
            phone=data.get("phone"),
            email=data.get("email"),
        )


__all__ = [
    "CreateHospitalRequest",
    "UpdateHospitalRequest",
]
