from django.core.management.base import BaseCommand

from services.workers import FillDatabaseCurrencyWorker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            FillDatabaseCurrencyWorker().fill()
            self.stdout.write(self.style.SUCCESS("Successfull"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
