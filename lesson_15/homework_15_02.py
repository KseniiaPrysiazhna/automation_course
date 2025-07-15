"""Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор
у файл json__<your_second_name>.log"""

import json
import logging
from pathlib import Path

json_dir = Path("/Users/andersen/Downloads/work_with_json")

log_file = Path(f"json_Prysiazhna.log")

logger = logging.getLogger("json_validator")
logger.setLevel(logging.ERROR)

if not logger.handlers:
    handler = logging.FileHandler(log_file, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

for json_file in json_dir.glob("*.json"):
    try:
        with open(json_file) as f:
            json.load(f)
    except Exception as e:
        logger.error(f"Файл '{json_file.name}' невалідний: {e}")

print(f"Перевірка завершена. Результати логування — у файлі: {log_file}")