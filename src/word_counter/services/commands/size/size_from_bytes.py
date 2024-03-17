from src.word_counter.commands.size.SizeUnits import SizeUnit


def size_from_bytes(size_in_bytes: int, output_unit: SizeUnit) -> float:
    if output_unit is SizeUnit.BYTES:
        return size_in_bytes

    unit_index_map: dict[str, int] = {
        unit: index
        for unit, index in zip(SizeUnit.values(), range(len(SizeUnit.values())))
    }

    conversion_factor = 1024 ** unit_index_map[output_unit.value]

    return round(size_in_bytes / conversion_factor, 4)
