from apps.currencies.repos import BaseRepository, CurrencyRepository, RateRepository

from apps.core.services.broker.serializers import BrokerSerializer


def update_currencies(
        currencies_data: bytes,
        serializer: BrokerSerializer = BrokerSerializer,
        repo: BaseRepository = CurrencyRepository
        ):
    currencies = serializer(currencies_data).serialize()
    repo().update_many(currencies)

def update_rates(
        rate_data: bytes,
        serializer: BrokerSerializer = BrokerSerializer,
        repo: BaseRepository = RateRepository
        ):
    rates = serializer(rate_data).serialize()
    repo().create_many(rates)