from confluent_kafka import Producer

from conf import KAFKA_CONFIG


class KafkaProducer:
    CONFIG = KAFKA_CONFIG

    def __init__(self, conf: dict[str, str] = CONFIG):
        self.__producer = Producer(conf)

    def send(self, topic: str, data: bytes):
        self.__producer.produce(topic, value=data)
        self.__producer.poll(1)
