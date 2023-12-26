import unittest

from newscorp.modules.data_modules import HitlogInputRow, HitlogOutputRow
from newscorp.modules.data_processor import (
    get_top_articles,
    process_influential_articles,
)


class TestProcessInfluentialArticles(unittest.TestCase):
    def test_process_influential_without_logs(self):
        input_rows = []

        output_rows = process_influential_articles(input_rows)

        self.assertEqual(len(output_rows), 0)

    def test_process_influential_with_just_register_log(self):
        input_rows = [
            HitlogInputRow(
                page_name="Registration",
                page_url="/register",
                user_id="user1",
                timestamp="2020-01-01 00:00:10",
            )
        ]

        output_rows = process_influential_articles(input_rows)

        self.assertEqual(len(output_rows), 0)

    def test_process_influential_articles_with_one_users(self):
        input_rows = [
            HitlogInputRow(
                page_name="Article 1",
                page_url="/articles/article#1",
                user_id="user1",
                timestamp="2020-01-01 00:00:10",
            ),
            HitlogInputRow(
                page_name="Registration",
                page_url="/register",
                user_id="user1",
                timestamp="2020-01-01 00:00:15",
            ),
        ]

        output_rows = process_influential_articles(input_rows)

        expected_output_rows = [
            HitlogOutputRow(
                page_name="Article 1", page_url="/articles/article#1", total=1
            ),
        ]

        self.assertEqual(
            output_rows[0].__dict__, expected_output_rows[0].__dict__
        )

    def test_process_influential_articles_with_three_users(self):
        input_rows = [
            HitlogInputRow(
                page_name="Article 2",
                page_url="/articles/article#2",
                user_id="user1",
                timestamp="2020-01-01 00:00:10",
            ),
            HitlogInputRow(
                page_name="Article 1",
                page_url="/articles/article#1",
                user_id="user1",
                timestamp="2020-01-01 00:00:20",
            ),
            HitlogInputRow(
                page_name="Article 3",
                page_url="/articles/article#3",
                user_id="user1",
                timestamp="2020-01-01 00:00:30",
            ),
            HitlogInputRow(
                page_name="Registration",
                page_url="/register",
                user_id="user1",
                timestamp="2020-01-01 00:00:40",
            ),
            HitlogInputRow(
                page_name="Article 1",
                page_url="/articles/article#1",
                user_id="user2",
                timestamp="2020-01-01 00:00:10",
            ),
            HitlogInputRow(
                page_name="Registration",
                page_url="/register",
                user_id="user2",
                timestamp="2020-01-01 00:00:40",
            ),
            HitlogInputRow(
                page_name="Article 2",
                page_url="/articles/article#2",
                user_id="user3",
                timestamp="2020-01-01 00:00:40",
            ),
            HitlogInputRow(
                page_name="Article 1",
                page_url="/articles/article#1",
                user_id="user3",
                timestamp="2020-01-01 00:00:50",
            ),
            HitlogInputRow(
                page_name="Registration",
                page_url="/register",
                user_id="user3",
                timestamp="2020-01-01 00:00:60",
            ),
        ]

        output_rows = process_influential_articles(input_rows)

        expected_output_rows = [
            HitlogOutputRow(
                page_name="Article 2", page_url="/articles/article#2", total=2
            ),
            HitlogOutputRow(
                page_name="Article 1", page_url="/articles/article#1", total=3
            ),
            HitlogOutputRow(
                page_name="Article 3", page_url="/articles/article#3", total=1
            ),
        ]

        for output_row, expected_output_row in zip(
            output_rows, expected_output_rows
        ):
            self.assertEqual(output_row.__dict__, expected_output_row.__dict__)


class TestGetTopArticles(unittest.TestCase):
    def test_get_top_articles_default(self):
        output_rows = [
            HitlogOutputRow(page_name="Page1", page_url="/page1", total=10),
            HitlogOutputRow(page_name="Page2", page_url="/page2", total=8),
            HitlogOutputRow(page_name="Page3", page_url="/page3", total=15),
            HitlogOutputRow(page_name="Page4", page_url="/page4", total=12),
            HitlogOutputRow(page_name="Page5", page_url="/page5", total=6),
        ]

        # Call the function with default parameter
        top_articles = get_top_articles(output_rows, 2)

        # Assertions to check the output
        self.assertIsInstance(top_articles, list)
        self.assertEqual(len(top_articles), 2)
        self.assertEqual(top_articles[0].total, 15)
        self.assertEqual(top_articles[1].total, 12)


if __name__ == "__main__":
    unittest.main()
