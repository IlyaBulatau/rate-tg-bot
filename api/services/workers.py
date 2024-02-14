from apps.currencies.repos import CurrencyRepository, RateRepository
from apps.currencies.models import Currency
from apps.currencies.serializers import CurrencySerializer, RateSerializer
from services.parser.parsers import CurrencyParser, RateParser, BaseParser
from services.domains import CurrencyDomain, RateDomain


class FillDatabaseCurrencyWorker:

    def fill(self):
        currencies: list[CurrencyDomain] = self.get_currencies()
        serializer = CurrencySerializer(
            data=[currency.to_dict() for currency in currencies], many=True
        )

        serializer.is_valid(raise_exception=True)

        CurrencyRepository().create_many(serializer.data)

    def get_currencies(
        self, parser: BaseParser = CurrencyParser
    ) -> list[CurrencyDomain]:
        currencies = parser().parse()
        return currencies


class FillDatabaseRateWorker:

    def fill(self, cur_abbreviation_array: list[str]):
        rates: list[RateDomain] = self.get_rates(cur_abbreviation_array)
        serializer = RateSerializer(data=[rate.to_dict() for rate in rates], many=True)

        serializer.is_valid(raise_exception=True)

        RateRepository().create_many(self._prepare_data_for_save(serializer.data))

    def _prepare_data_for_save(self, data: list[dict]) -> list[tuple[Currency, dict]]:
        save_data = []

        for item in data:
            currency_abbreviation: str = item.pop("currency_abbreviation")
            currency_obj: Currency = CurrencyRepository().get_by_abbreviation(
                currency_abbreviation
            )
            save_data.append((currency_obj, item))

        return save_data

    def get_rates(
        self, cur_abbreviation_array: list[str], parser: BaseParser = RateParser
    ) -> list[RateDomain]:
        rates = parser().parse_many(cur_abbreviation_array)
        return rates
