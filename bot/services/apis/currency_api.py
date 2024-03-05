from aiohttp import ClientSession

import sys

import config as conf


class APIClient:
    BASE_URL = None
    HEADERS = None

    def __init__(self, session: ClientSession = ClientSession):
        self.__async_session = session
    
    async def async_session(self):
        async with self.__async_session() as client:
            try:
                yield client
            finally:
                yield
                await client.close()


class APICurrencyClient(APIClient):

    BASE_URL = conf.API_SERVICE_URL
    HEADERS = {"Authorization": "Bearer "+conf.API_AUTH_TOKEN}
    

    async def get_rate(self, abbreviation: str, query_params: dict = None) -> list[dict] | dict:
        endpoint = f"/currencies/rates/{abbreviation}"
        url = self.BASE_URL+endpoint
        session = await self.async_session().__anext__()

        async with session.get(url, headers=self.HEADERS) as response:
            if response.status == 200:
                return await response.json()
            body = await response.text()
            sys.stdout.write(str(body))
            return None
