from dataclasses import dataclass, asdict
from datetime import date


class DataclassToDict:

    def to_dict(self):
        return asdict(self)

@dataclass(kw_only=True, eq=True, frozen=True)
class CurrencyDomain(DataclassToDict):
    abbreviation: str # буквенный код
    name_ru: str # наименование валюты на русском языке
    name_eng: str # наименование на английском языке
    scale: int # количество единиц иностранной валюты

    def __hash__(self) -> int:
        return hash(self.abbreviation)

    def __eq__(self, other) -> bool:
        if not isinstance(other, CurrencyDomain):
            return False
        return self.abbreviation == other.abbreviation

@dataclass(kw_only=True, eq=True, frozen=True)
class RateDomain(DataclassToDict):
    cur_abbreviation: str
    date: date #  дата, на которую запрашивается курс
    rate: float # курс

    def __hash__(self) -> int:
        return hash(self.cur_abbreviation)

    def __eq__(self, other) -> bool:
        if not isinstance(other, RateDomain):
            return False
        return self.cur_abbreviation == other.cur_abbreviation
