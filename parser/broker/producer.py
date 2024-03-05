import pika
from pika.adapters.blocking_connection import BlockingChannel

import conf


class BrokerProducer:

    def __init__(self):
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host="broker",
                port=5672,
                credentials=pika.PlainCredentials(
                    username=conf.BROKER_USER,
                    password=conf.BROKER_PASSWORD
                    )
                )
            )
        self._channel: BlockingChannel = self._connection.channel()

        self._channel.queue_declare(queue=conf.QUEUE_CURRENCY, durable=True)

    def send(self, content_type, message: bytes):
        properties = pika.BasicProperties(content_type=content_type)
        self._channel.basic_publish(
            exchange="",
            routing_key=conf.QUEUE_CURRENCY,
            body=message,
            properties=properties
            )