from enum import Enum


class OutputFormats(Enum):
    JSON = "json"
    YAML = "yaml"
    TOML = "toml"
    XML = "xml"
    PLAINTEXT = "plaintext"

    @classmethod
    def values(cls) -> list[str]:
        return [format_.value for format_ in cls._member_map_.values()]
