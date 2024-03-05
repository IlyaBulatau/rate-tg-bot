import pika 
from pika.adapters.blocking_connection import BlockingChannel

import sys

from apps.core.services.broker import conf
from apps.core.services.use_case import update_currencies, update_rates


class BrokerConsumer:

    EVENTS ={
        "currency": update_currencies,
        "rate": update_rates,
    }

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
        self._channel.basic_consume(queue=conf.QUEUE_CURRENCY, on_message_callback=self.callback, auto_ack=True)

    
    def callback(self, ch: BlockingChannel, method, properties: pika.BasicProperties, body: bytes):
        event = self.EVENTS[properties.content_type]
        event(body)
        sys.stdout.write(f"Обработаны данные типа {properties.content_type}")


    def run(self):
        self._channel.start_consuming()
        sys.stdout.write(f"Консьюмер слушает очередь {conf.QUEUE_CURRENCY}")
        self._channel.start_consuming()
        self._channel.close()