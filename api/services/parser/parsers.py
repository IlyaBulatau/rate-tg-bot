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
                idx=item.get("Cur_ID"),
                code=item.get("Cur_Code"),
                abbreviation=item.get("Cur_Abbreviation"),
                name_ru=item.get("Cur_Name"),
                name_eng=item.get("Cur_Name_Eng"),
                scale=item.get("Cur_Scale")
            )
            for item in data
        ]
        return result

class RateParser(BaseParser):
    URI = "exrates/rates/{cur_idx}"

    def parse(self, cur_idx: int) -> RateDomain:
        with requests.Session() as session:
            response = session.get(self.get_url.format(cur_idx=cur_idx))
        
        data = self._prepare_data(response.json())
        return data

    def parse_many(self, array_cur_idx: list[int]) -> list[RateDomain]:
        rate_set: list[RateDomain] = []
        
        with requests.Session() as session:
            for cur_idx in array_cur_idx:
                response = session.get(self.get_url.format(cur_idx=cur_idx))
                rate_set.append(self._prepare_data(response.json()))
        
        return rate_set

    def _prepare_data(self, data: dict) -> RateDomain:
        return RateDomain(
            cur_idx=data.get("Cur_ID"),
            date=data.get("Date"),
            rate=data.get("Cur_OfficialRate")
        )
