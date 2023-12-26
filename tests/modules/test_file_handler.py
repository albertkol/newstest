import os
import unittest
from dataclasses import dataclass

from newscorp.modules.data_modules import Row
from newscorp.modules.file_handler import read_file, write_file
from tests.helpers import create_test_file


class TestReadFile(unittest.TestCase):
    def setUp(self):
        # Set the test file path
        self.test_file_path = "./tests/modules/test_data.csv"

    def tearDown(self):
        # Delete the test file after each test, if it exists
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_read_file_handles_empty_file(self):
        empty_file_content = []
        create_test_file(self.test_file_path, empty_file_content)

        rows = read_file(self.test_file_path, Row)

        self.assertEqual(rows, [])

    def test_read_file_handles_columns(self):
        # defining a dummy row class
        @dataclass
        class TestColumnsRow(Row):
            col1: str
            col2: str

        csv_content = [
            {"col1": "value1", "col2": "value2"},
            {"col1": "value1", "col2": "value2"},
        ]

        create_test_file(self.test_file_path, csv_content)

        rows = read_file(self.test_file_path, TestColumnsRow)

        self.assertEqual(len(rows), 2)
        for row in rows:
            self.assertIsInstance(row, TestColumnsRow)

    def test_read_file_handles_missing_columns(self):
        # defining a dummy row class
        @dataclass
        class TestColumnsRow(Row):
            col1: str
            col2: str

        csv_content = [
            {"col1": "value1", "col2": "value2"},
            {"col1": "value1"},
        ]

        create_test_file(self.test_file_path, csv_content)

        rows = read_file(self.test_file_path, TestColumnsRow)

        self.assertEqual(len(rows), 2)
        for row in rows:
            self.assertIsInstance(row, TestColumnsRow)

        self.assertEqual(rows[1].col2, "")

    def test_read_file_handles_incorrect_row_structure(self):
        # defining a dummy row class without col2
        @dataclass
        class TestColumnsRow(Row):
            col1: str

        csv_content = [
            {"col1": "value1", "col2": "value2"},
        ]

        create_test_file(self.test_file_path, csv_content)

        with self.assertRaises(TypeError):
            read_file(self.test_file_path, TestColumnsRow)


class TestWriteFile(unittest.TestCase):
    def setUp(self):
        # Set the test file path
        self.test_file_path = "./tests/modules/test_data.csv"

    def tearDown(self):
        # Delete the test file after each test, if it exists
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_write_file_handles_no_content(self):
        no_content = []

        write_file(self.test_file_path, no_content)

        self.assertTrue(os.path.exists(self.test_file_path))

    def test_write_file_with_rows(self):
        # defining a dummy row class
        @dataclass
        class TestColumnsRow(Row):
            col1: str
            col2: str

        rows = [
            TestColumnsRow(col1="value1", col2="value2"),
            TestColumnsRow(col1="value1", col2="value2"),
        ]

        write_file(self.test_file_path, rows)

        self.assertTrue(os.path.exists(self.test_file_path))

        with open(self.test_file_path, newline="") as csv_file:
            file_content = csv_file.read()

        self.assertEqual(
            file_content,
            "col1,col2\r\nvalue1,value2\r\nvalue1,value2\r\n",
        )


if __name__ == "__main__":
    unittest.main()
