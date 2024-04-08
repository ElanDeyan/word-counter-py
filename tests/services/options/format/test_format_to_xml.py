from hypothesis import given
import xml.etree.ElementTree as ET

from src.word_counter.services.options.format.file_data_to_xml_element import (
    format_to_xml,
)
from .hypothesis import lists_of_dicts


# @given(files_data=lists_of_dicts)
# def test_format_to_xml(files_data: list[dict[str, object]]):
#     assert isinstance(ET.fromstring(format_to_xml(files_data)), ET.ElementTree)
