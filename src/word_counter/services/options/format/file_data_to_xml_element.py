from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, SubElement, tostring as xml_to_str


def file_data_to_xml_element(file_data: dict[str, object]) -> Element:
    """
    The function `file_data_to_xml_element` converts a dictionary of file data into an XML element.
    
    :param file_data: A dictionary containing data that you want to convert to an XML element. The keys
    represent the tags in the XML element, and the values represent the text content of those tags
    :type file_data: dict[str, object]
    :return: An XML element representing the file data in the dictionary.
    """
    root = Element("FileData")

    for key, value in file_data.items():
        child = SubElement(root, key)
        child.text = str(value)

    return root


def format_to_xml(data: list[dict[str, object]]) -> str:
    """
    The function `format_to_xml` converts a list of dictionaries into an XML string and returns a
    prettified version of the XML.
    
    :param data: The `data` parameter is a list of dictionaries where each dictionary represents file
    data. Each dictionary should have keys and values that you want to convert to XML elements
    :type data: list[dict[str, object]]
    :return: The function `format_to_xml` returns a pretty-printed XML string representation of the data
    provided in the list of dictionaries.
    """
    root = Element("FileDataList")

    for file_data in data:
        element = file_data_to_xml_element(file_data)
        root.append(element)

    xml_str = xml_to_str(root, encoding="utf-8")

    dom = parseString(xml_str)

    return dom.toprettyxml()
