from services.apis.currency_api import APICurrencyClient

async def get_all_currency(
        _filters: dict = None,
        api_client: APICurrencyClient = APICurrencyClient,
    ):
    client = api_client()
    currencies = await client.get_currency(_filters)
    return currencies

async def get_currency_by_abbreviation(
        abbreviation: list[str] | str,
        api_client: APICurrencyClient = APICurrencyClient,
        ):
    ...