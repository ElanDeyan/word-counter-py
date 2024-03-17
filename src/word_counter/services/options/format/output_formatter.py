import json
import yaml
from tabulate import tabulate
from src.word_counter.options.format.OutputFormats import OutputFormats
from src.word_counter.utils.serialize_to_toml import format_to_toml
from src.word_counter.services.options.format.file_data_to_xml_element import (
    format_to_xml,
)


def output_formatter(data: list[dict[str, object]], format_: OutputFormats) -> str:
    serialized_data = [dict(file_data) for file_data in data]

    match format_:
        case OutputFormats.JSON:
            return json.dumps(serialized_data, indent=4)
        case OutputFormats.YAML:
            return yaml.dump(serialized_data)
        case OutputFormats.TOML:
            return format_to_toml(serialized_data)
        case OutputFormats.XML:
            return format_to_xml(serialized_data)
        case OutputFormats.PLAINTEXT:
            return tabulate(serialized_data, headers="keys", tablefmt="pretty")
