"""Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv
порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv"""

from pathlib import Path
import csv

base_dir = Path("/Users/andersen/Downloads")

file1 = base_dir / "random.csv"
file2 = base_dir / "random-michaels.csv"
output_file = base_dir / "results_Prysiazhna.csv"

rows = set()

for file in [file1, file2]:
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            rows.add(tuple(row))

with open(output_file, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in sorted(rows):
        writer.writerow(row)

print(f"Файл без дублікатів записано в: {output_file}")