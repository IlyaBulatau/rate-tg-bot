from datetime import date, datetime
from dateutil import parser


def from_iso_str_to_date(str_date: str) -> date:
    result: datetime = parser.isoparse(str_date)
    return result.date()
