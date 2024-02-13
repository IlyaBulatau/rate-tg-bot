from apps.currencies.repos import CurrencyRepository
from apps.currencies.serializers import CurrencySerializer
from services.parser.parsers import CurrencyParser, RateParser, BaseParser
from services.parser.domains import CurrencyDomain, RateDomain


class FillDatabaseCurrencyWorker:

    def fill(self):
        currencies: list[CurrencyDomain] = self.get_currencies()
        serializer = CurrencySerializer(data=[currency.to_dict() for currency in currencies], many=True)
        
        if not serializer.is_valid():
            raise Exception()

        CurrencyRepository().create_many(serializer.data)

    def get_currencies(self, parser: BaseParser = CurrencyParser) -> list[CurrencyDomain]:
        currencies = parser().parse()
        return currencies


class FillDatabaseRateWorker:

    def fill(self, cur_abbreviation: int):
        ...
    
    def get_rates(self, cur_abbreviation: int, parser: BaseParser = RateParser) -> list[RateDomain]:
        rates = parser().parse(cur_abbreviation)
        return rates