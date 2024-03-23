from src.word_counter.utils.SizeUnits import SizeUnit


def filesize(content: str, output_unit: SizeUnit) -> str:
    size_in_bytes = len(content.encode())

    if output_unit is SizeUnit.BYTES:
        return f"{size_in_bytes}B"

    unit_index_map: dict[str, int] = {
        unit: index
        for unit, index in zip(SizeUnit.values(), range(len(SizeUnit.values())))
    }

    conversion_factor = 1024 ** unit_index_map[output_unit.value]
    return f"{round(size_in_bytes / conversion_factor, 2)} {output_unit.value}"
