import csv
from typing import List

from newscorp.modules.data_modules import Row


def read_file(file_path: str, row_class: Row) -> List[Row]:
    rows = []
    with open(file_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            input_row = row_class(**row)
            rows.append(input_row)

    return rows


def write_file(file_path: str, rows: List[Row]) -> None:
    column_names = rows[0].__annotations__.keys() if rows else []
    with open(file_path, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=column_names)
        writer.writeheader()

        # Write rows to the CSV file
        for row in rows:
            writer.writerow(row.__dict__)
