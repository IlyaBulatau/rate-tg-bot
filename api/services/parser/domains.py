from dataclasses import dataclass
from datetime import date


@dataclass(kw_only=True)
class CurrencyDomain:
    idx: int # внутренний код
    code: int # цифровой код 
    abbreviation: str # буквенный код
    name_ru: str # наименование валюты на русском языке
    name_eng: str # наименование на английском языке
    scale: int # количество единиц иностранной валюты

@dataclass(kw_only=True)
class RateDomain:
    cur_idx: int
    date: date #  дата, на которую запрашивается курс
    rate: float # курс