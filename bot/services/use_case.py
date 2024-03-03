from services.apis.currency_api import APICurrencyClient
from domains.currencies import AvalibaleCurrency
from domains.dto import ExchangeRate


async def get_rate_by_abbreviation(
        abbreviation: AvalibaleCurrency,
        api_client: APICurrencyClient = APICurrencyClient,
        ):
    client = api_client()
    data = await client.get_rate(abbreviation)
    rate = ExchangeRate(**data)
    return rate