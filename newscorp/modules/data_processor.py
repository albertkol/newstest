from collections import defaultdict
from typing import List

from newscorp.modules.data_modules import HitlogInputRow, HitlogOutputRow


def process_influential_articles(
    input_rows: List[HitlogInputRow],
) -> List[HitlogOutputRow]:
    output_rows = defaultdict()
    # Dictionary to track user journeys
    user_journeys = defaultdict(list)

    for input_row in input_rows:
        # If row is an article visit log add it to user's journey
        if input_row.page_url != "/register":
            # Append input_row to user's journey
            user_journeys[input_row.user_id].append(input_row)

            continue

        # Row is a registration log
        # Count previous page visits leading to registration
        for log in user_journeys[input_row.user_id]:
            current_total = (
                output_rows[log.page_url].total
                if log.page_url in output_rows
                else 0
            )

            output_rows[log.page_url] = HitlogOutputRow(
                page_name=log.page_name,
                page_url=log.page_url,
                total=current_total + 1,
            )

        # Reset user's journey after registration
        user_journeys[input_row.user_id] = []

    return list(output_rows.values())


def get_top_articles(
    output_rows: List[HitlogOutputRow],
    how_many: int = 3,
) -> List[HitlogOutputRow]:
    return sorted(output_rows, key=lambda x: x.total, reverse=True)[:how_many]
