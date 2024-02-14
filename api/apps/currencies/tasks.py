from services.workers import FillDatabaseRateWorker
from apps.currencies.repos import CurrencyRepository
from settings import celery_app

from celery.schedules import crontab


@celery_app.task
def fill_rate_table_data():
    currencies_abbrs: list[str] = CurrencyRepository().get_currencies_abbr()
    FillDatabaseRateWorker().fill(currencies_abbrs)


celery_app.conf.beat_schedule = {
    "parse_and_save_rates": {
        "task": "apps.currencies.tasks.fill_rate_table_data",
        "schedule": crontab(hour=12, minute=3)
    }
}