from os import getenv as ENV
from datetime import time

BROKER_USER = ENV("BROKER_USER")
BROKER_PASSWORD = ENV("BROKER_PASSWORD")
QUEUE_CURRENCY = ENV("QUEUE_CURRENCY")

UPDATE_CURRENCY_TIME = time(hour=12, minute=2)
