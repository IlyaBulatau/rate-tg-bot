from os import getenv as ENV
from datetime import time


KAFKA_CONFIG = {"bootstrap.servers": "kafka:9092"}
KAFKA_CURRENCY_TOPIC = ENV("KAFKA_CURRENCY_TOPIC", "currency")
KAFKA_RATE_TOPIC = ENV("KAFKA_RATE_TOPIC", "rate")

UPDATE_CURRENCY_TIME = time(hour=12, minute=2)