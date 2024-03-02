from apps.currencies.repos import BaseRepository, CurrencyRepository, RateRepository
from apps.core.services.kafka.serializers import BaseKafkaSerializer, CurrencyKafkaSerializer, RateKafkaSerializer


def update_currencies(
        currencies_data: bytes,
        serializer: BaseKafkaSerializer = CurrencyKafkaSerializer,
        repo: BaseRepository = CurrencyRepository()
        ):
    currencies: list[dict] = serializer(currencies_data).serialize()
    repo.update_many(currencies)

def update_rates(
        rate_data: bytes,
        serializer: BaseKafkaSerializer = RateKafkaSerializer,
        repo: BaseRepository = RateRepository
        ):
    rates: list[dict] = serializer(rate_data).serialize()
    # repo.update_many(currencies)
