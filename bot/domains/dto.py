from dataclasses import dataclass
from datetime import date


@dataclass(kw_only=True, unsafe_hash=True)
class ExchangeRate:
    date: date
    rate: float
    currency_abbreviation: str
    name_ru: str
    name_eng: str
    scale: int