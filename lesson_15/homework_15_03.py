"""Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку
по group/number і повернення значення timingExbytes/incoming
результат виведіть у консоль через логер на рівні інфо"""

import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger("log_event")
logger.setLevel(logging.INFO)
if not logger.handlers:
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

def find_incoming_by_group_number(xml_path, group_number):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall('group'):
        number_elem = group.find('number')
        if number_elem is not None and number_elem.text == str(group_number):
            incoming = group.find('timingExbytes/incoming')
            if incoming is not None:
                logger.info(f"Group number: {group_number}, incoming: {incoming.text}")
                return incoming.text
            else:
                logger.info(f"Group number: {group_number}, incoming: Не знайдено")
                return None

    logger.info(f"Group з number={group_number} не знайдено")
    return None

if __name__ == "__main__":
    xml_path = '/Users/andersen/Downloads/groups.xml'
    group_num = 2

    find_incoming_by_group_number(xml_path, group_num)