import requests
from abc import ABC, abstractmethod

from domains import CurrencyDomain, RateDomain


class BaseParser(ABC):
    ROOT_DOMAIN = "https://api.nbrb.by/"
    URI = None

    @abstractmethod
    def parse(self) -> list[object]:
        ...
    
    @property
    def get_url(self) -> str:
        return self.ROOT_DOMAIN + self.URI


class CurrencyParser(BaseParser):
    URI = "exrates/currencies/"

    def parse(self) -> list[CurrencyDomain]:
        with requests.Session() as session:
            response = session.get(self.get_url)
        
        data = self._prepare_data(response.json())
        return data
        
    def _prepare_data(self, data: list[dict]) -> list[CurrencyDomain]:
        result = [
            CurrencyDomain(
                abbreviation=item.get("Cur_Abbreviation"),
                name_ru=item.get("Cur_Name"),
                name_eng=item.get("Cur_Name_Eng"),
                scale=item.get("Cur_Scale")
            )
            for item in data
        ]
        return result

class RateParser(BaseParser):
    URI = "exrates/rates/{cur_abbreviation}?parammode=2"

    def parse(self, cur_abbreviation: str) -> RateDomain:
        with requests.Session() as session:
            response = session.get(self.get_url.format(cur_abbreviation=cur_abbreviation))
        
        data = self._prepare_data(response.json())
        return data

    def parse_many(self, array_cur_abbreviation: list[str]) -> list[RateDomain]:
        rate_set: list[RateDomain] = []
        
        with requests.Session() as session:
            for cur_abbreviation in array_cur_abbreviation:
                response = session.get(self.get_url.format(cur_abbreviation=cur_abbreviation))
                rate_set.append(self._prepare_data(response.json()))
        
        return rate_set

    def _prepare_data(self, data: dict) -> RateDomain:
        return RateDomain(
            cur_abbreviation=data.get("Cur_Abbreviation"),
            date=data.get("Date"),
            rate=data.get("Cur_OfficialRate")
        )
