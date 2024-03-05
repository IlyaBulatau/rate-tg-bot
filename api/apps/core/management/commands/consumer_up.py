from django.core.management import BaseCommand

from apps.core.services.broker.consumer import BrokerConsumer


class Command(BaseCommand):

    def handle(self, *args, **options) -> str | None:
        consumer = BrokerConsumer()
        consumer.run()