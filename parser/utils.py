from datetime import datetime
from dateutil import parser


def from_iso_str_to_date(str_date: str) -> str:
    result: datetime = parser.isoparse(str_date)
    return result.date().strftime("%Y-%m-%d")
