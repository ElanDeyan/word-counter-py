from enum import Enum


class OutputFormats(Enum):
    """
    The class `OutputFormats` defines an enumeration for different output formats and provides a method
    to retrieve a list of string values from the enumeration.
    """

    JSON = "json"
    YAML = "yaml"
    TOML = "toml"
    XML = "xml"
    PLAINTEXT = "plaintext"

    @classmethod
    def values(cls) -> list[str]:
        """
        This function returns a list of values from an enum class.

        :param cls: The `cls` parameter in the given function represents a class object
        :return: A list of string values from the `_member_map_` attribute of the class `cls` is being
        returned.
        """
        return [format_.value for format_ in cls._member_map_.values()]
