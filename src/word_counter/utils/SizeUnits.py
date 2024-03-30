from enum import Enum
from typing import NamedTuple


class SizeUnitData(NamedTuple):
    short_name: str
    conversion_from_bytes_factor: float


class SizeUnit(Enum):
    BYTES = SizeUnitData(short_name="B", conversion_from_bytes_factor=1)
    KILOBYTES = SizeUnitData(short_name="KB", conversion_from_bytes_factor=(1024**1))
    MEGABYTES = SizeUnitData(short_name="MB", conversion_from_bytes_factor=(1024**2))
    GIGABYTES = SizeUnitData(short_name="GB", conversion_from_bytes_factor=(1024**3))
    TERABYTES = SizeUnitData(short_name="TB", conversion_from_bytes_factor=(1024**4))

    @classmethod
    def short_names(cls) -> list[str]:
        return [unit.value.short_name for unit in cls._member_map_.values()]
