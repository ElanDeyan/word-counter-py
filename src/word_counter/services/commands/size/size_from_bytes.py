from src.word_counter.commands.size.SizeUnits import SizeUnit


def size_from_bytes(size_in_bytes: int, output_unit: SizeUnit) -> float:
    size: float

    match output_unit:
        case SizeUnit.BYTES:
            size = float(size_in_bytes)
        case SizeUnit.KILOBYTES:
            size = size_in_bytes / 1e3
        case SizeUnit.MEGABYTES:
            size = size_in_bytes / 1e6
        case SizeUnit.GIGABYTES:
            size = size_in_bytes / 1e9
        case SizeUnit.TERABYTES:
            size = size_in_bytes / 1e12
    return size
