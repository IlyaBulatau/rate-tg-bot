from enum import Enum

from django.conf import settings


class Topic(Enum):
    CURRENCY = "currency" if not settings.KAFKA_CURRENCY_TOPIC else settings.KAFKA_CURRENCY_TOPIC

    @classmethod
    def to_list(cls):
        return [item.value for item in cls]
    
CONFIG = {
    "bootstrap.servers": f"{settings.KAFKA_HOST}:9092", 
    'auto.offset.reset': 'smallest', 
    'group.id': "app",
    }