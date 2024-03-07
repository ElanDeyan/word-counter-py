from enum import Enum


class SizeUnit(Enum):
    BYTES = "B"
    KILOBYTES = "KB"
    MEGABYTES = "MB"
    GIGABYTES = "GB"
    TERABYTES = "TB"

    @classmethod
    def values(cls) -> list[str]:
        return [unit.value for unit in SizeUnit._member_map_.values()]
