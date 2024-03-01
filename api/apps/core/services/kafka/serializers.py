from abc import ABC, abstractmethod
import json
import datetime


class BaseKafkaSerializer(ABC):

    def __init__(self, data: bytes):
        self.data = data
    
    @abstractmethod
    def serialize(self):
        ...

    def _prepare(self) -> str:
        """Bytes to str"""
        return  self.data.decode()


class CurrencyKafkaSerializer(BaseKafkaSerializer):
    
    def serialize(self) -> list[dict]:
        data_to_str: str = self._prepare()
        data = json.loads(data_to_str.replace("'", '"'))
        return data


class RateKafkaSerializer(BaseKafkaSerializer):

    def serialize(self) -> list[dict]:
        data_to_str: str = self._prepare()
        data = eval(data_to_str.replace("'", '"'))
        return data
