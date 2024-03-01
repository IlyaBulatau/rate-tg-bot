from django.core.management import BaseCommand

from apps.core.services.kafka.consumer import KafkaConsumer

class Command(BaseCommand):

    def handle(self, *args, **options) -> str | None:
        KafkaConsumer().run()