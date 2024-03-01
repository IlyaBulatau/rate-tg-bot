from confluent_kafka import Consumer, KafkaException

from typing import Callable
from logging import getLogger

from apps.core.services.kafka.conf import Topic, CONFIG
from apps.core.services.use_case import update_currencies


log = getLogger(__name__)

class KafkaConsumer:
    TOPICS = Topic.to_list()

    def __init__(
            self,
            conf: dict[str, str] = CONFIG,
            topics: list[str] = TOPICS,
            process: Callable = update_currencies,
            ):
        self.__consumer = Consumer(conf)
        self.topics = topics
        self.process = process

    def run(self):
        try:
            self.__consumer.subscribe(self.topics)
            while True:
                message = self.__consumer.poll(timeout=1.0)
                if not message: 
                    continue

                if message.error():
                    raise KafkaException(message.error())
                else:
                    self.process(message)
        finally:
            self.__consumer.close()