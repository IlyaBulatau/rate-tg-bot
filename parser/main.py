import requests
from abc import ABC, abstractmethod
from datetime import datetime
import pytz
import time
import sys

from utils import from_iso_str_to_date
from domains import CurrencyDomain, RateDomain
import conf
from kafka.producer import KafkaProducer


class BaseParser(ABC):
    ROOT_DOMAIN = "https://api.nbrb.by/"
    URI = None

    @abstractmethod
    def parse(self) -> list[object]: ...

    @property
    def get_url(self) -> str:
        return self.ROOT_DOMAIN + self.URI


class CurrencyParser(BaseParser):
    URI = "exrates/currencies/"

    def parse(self) -> list[CurrencyDomain]:
        with requests.Session() as session:
            response = session.get(self.get_url)

        data = self._prepare_data(response.json())
        return data

    def _prepare_data(self, data: list[dict]) -> list[CurrencyDomain]:
        result = [
            CurrencyDomain(
                abbreviation=item.get("Cur_Abbreviation"),
                name_ru=item.get("Cur_Name"),
                name_eng=item.get("Cur_Name_Eng"),
                scale=item.get("Cur_Scale"),
            )
            for item in data
        ]
        return list(set(result))


class RateParser(BaseParser):
    URI = "exrates/rates/{cur_abbreviation}?parammode=2"

    def parse(self, cur_abbreviation: str) -> RateDomain:
        with requests.Session() as session:
            response = session.get(
                self.get_url.format(cur_abbreviation=cur_abbreviation)
            )

        data = self._prepare_data(response.json())
        return data

    def parse_many(self, array_cur_abbreviation: list[str]) -> list[RateDomain]:
        rate_set: list[RateDomain] = []

        with requests.Session() as session:
            for cur_abbreviation in array_cur_abbreviation:
                response = session.get(
                    self.get_url.format(cur_abbreviation=cur_abbreviation)
                )
                data = self._prepare_data(response.json())
                if data.currency_abbreviation:
                    rate_set.append(data)

        return rate_set

    def _prepare_data(self, data: dict) -> RateDomain:
        return RateDomain(
            currency_abbreviation=data.get("Cur_Abbreviation"),
            date=from_iso_str_to_date(date) if (date := data.get("Date")) else date,
            rate=data.get("Cur_OfficialRate"),
        )

    @staticmethod
    def collect_abbreviations(data: list[CurrencyDomain]) -> list[str]:
        return [item.abbreviation for item in data]


if __name__ == "__main__":
    sys.stdout.write("Парсер поднялся")
    currency_parser = CurrencyParser()
    rate_parser = RateParser()
    producer = KafkaProducer()

    while True:
        time.sleep(3)
        dt_now = datetime.now(pytz.timezone("Europe/Minsk")).time()
        if (
            dt_now.hour == conf.UPDATE_CURRENCY_TIME.hour
            and dt_now.minute == conf.UPDATE_CURRENCY_TIME.minute
        ):
            currency_data = currency_parser.parse()
            rate_data = rate_parser.parse_many(
                rate_parser.collect_abbreviations(currency_data)
            )

            currency_bytes = str([data.to_dict() for data in currency_data]).encode()
            rate_bytes = str([data.to_dict() for data in rate_data]).encode()

            producer.send(conf.KAFKA_CURRENCY_TOPIC, currency_bytes)
            producer.send(conf.KAFKA_RATE_TOPIC, rate_bytes)
