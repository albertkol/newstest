import csv
from io import StringIO


def create_test_file(test_file_path: str, csv_content: dict) -> None:
    csv_file = StringIO()

    column_names = csv_content[0].keys() if csv_content else []

    writer = csv.DictWriter(csv_file, fieldnames=column_names)
    writer.writeheader()
    writer.writerows(csv_content)

    csv_file.seek(0)

    with open(test_file_path, "w") as file:
        file.write(csv_file.getvalue())
