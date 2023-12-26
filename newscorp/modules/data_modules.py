from dataclasses import dataclass


@dataclass
class Row:
    pass


@dataclass
class HitlogInputRow(Row):
    page_name: str
    page_url: str
    user_id: str
    timestamp: str


@dataclass
class HitlogOutputRow(Row):
    page_name: str
    page_url: str
    total: int
