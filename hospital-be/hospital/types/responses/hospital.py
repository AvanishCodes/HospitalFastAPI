from dataclasses import dataclass
from typing import Optional
from ..entities import Hospital


@dataclass
class GetHospitalsResponse:
    hospitals: Optional[list[Hospital]]

    @property
    def to_dict(self) -> dict[str, list[dict[str, int | str | None]] | None]:
        return {
            "hospitals": (
                [hospital.to_dict for hospital in self.hospitals]
                if self.hospitals
                else None
            )
        }


__all__ = [
    "GetHospitalsResponse",
]
