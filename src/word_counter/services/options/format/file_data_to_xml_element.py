from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, SubElement, tostring as xml_to_str


def file_data_to_xml_element(file_data: dict[str, object]) -> Element:
    root = Element("FileData")

    for key, value in file_data.items():
        child = SubElement(root, key)
        child.text = str(value)

    return root


def format_to_xml(data: list[dict[str, object]]) -> str:
    root = Element("FileDataList")

    for file_data in data:
        element = file_data_to_xml_element(file_data)
        root.append(element)

    xml_str = xml_to_str(root, encoding="utf-8")

    dom = parseString(xml_str)

    return dom.toprettyxml()
