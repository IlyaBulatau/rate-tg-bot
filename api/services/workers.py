from django.db.models import Model

from services.parser.parsers import CurrencyParser, RateParser, BaseParser
from services.parser.domains import CurrencyDomain, RateDomain


class FillDatabaseCurrencyWorker:

    def fill(self):
        ...
    
    def get_currencies(self, parser: BaseParser = CurrencyParser) -> list[CurrencyDomain]:
        currencies = parser.parse()
        return currencies
    

class FillDatabaseRateWorker:

    def fill(self, cur_abbreviation: int):
        ...
    
    def get_rates(self, cur_abbreviation: int, parser: BaseParser = RateParser) -> list[RateDomain]:
        rates = parser.parse(cur_abbreviation)
        return rates