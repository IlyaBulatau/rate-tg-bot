from apps.currencies.repos import BaseRepository, CurrencyRepository

from logging import getLogger


log = getLogger(__name__)


def update_currencies(
        currencies_data: bytes, 
        repo: BaseRepository = CurrencyRepository
        ):
    log.warning(currencies_data)