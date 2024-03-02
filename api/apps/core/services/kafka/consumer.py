from confluent_kafka import Consumer, KafkaException

from typing import Callable
import sys
import datetime

from apps.core.services.kafka.conf import Topic, CONFIG
from apps.core.services.use_case import update_currencies, update_rates


class ConsumerProcessDefiner:

    processes = {
        Topic.CURRENCY.value: update_currencies,
        Topic.RATE.value: update_rates
    }

    def define(self, topic: str):
        return self.processes.get(topic, None)


class KafkaConsumer:
    TOPICS = Topic.to_list()

    def __init__(
            self,
            conf: dict[str, str] = CONFIG,
            topics: list[str] = TOPICS,
            processs_definer: Callable = ConsumerProcessDefiner,
            ):
        self.__consumer = Consumer(conf)
        self.topics = topics
        self.processs_definer = processs_definer()

    def run(self):
        try:
            self.__consumer.subscribe(self.topics)
            while True:
                message = self.__consumer.poll(timeout=1.0)
                if not message: 
                    continue

                if message.error():
                    sys.stdout.writable(f"Ошибка при чтении данных с топика {message.topic()}")
                    raise KafkaException(message.error())
                else:
                    process = self.processs_definer.define(message.topic())
                    process(message.value())
                    sys.stdout.write(f"Курс обновлен, Время: {datetime.datetime.now().strftime('%Y-%B-%d %H:%M')}\n")
        finally:
            self.__consumer.close()


