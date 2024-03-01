from abc import ABC, abstractmethod


class BaseKafkaSerializer(ABC):

    def __init__(self, data: bytes):
        self.data = data
    
    @abstractmethod
    def serialize(self):
        ...

    def _prepare(self) -> list[dict]:
        return


class CurrencyKafkaSerializer(BaseKafkaSerializer):
    ...

class RateKafkaSerializer(BaseKafkaSerializer):
    ...