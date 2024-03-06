from abc import ABC, abstractmethod

from django.db import models, transaction

from .models import Currency, Rate


class BaseRepository(ABC):
    model = None

    @abstractmethod
    def create(self) -> models.Model: ...

    @abstractmethod
    def get_all(self) -> models.Model: ...

    @abstractmethod
    def delete(self) -> None: ...


class ModelRepository(BaseRepository):

    def __init__(self, model: models.Model | None = None):
        if model:
            self.model = model

    def create(self, data: dict) -> models.Model:
        obj = self.model.objects.create(**data)
        return obj

    def create_many(self, datas: list[dict]) -> None:
        self.model.objects.bulk_create([self.model(**data) for data in datas])

    def get_all(self) -> models.QuerySet[models.Model]:
        return self.model.objects.all()

    def delete(self) -> None: ...


class CurrencyRepository(ModelRepository):
    model = Currency

    def get_all(self) -> models.QuerySet[models.Model]:
        return self.model.objects.only(
            "abbreviation", "name_ru", "name_eng"
        ).all()

    def get_currencies_abbr(self) -> list[str]:
        result = self.model.objects.values_list("abbreviation", flat=True)
        return list(result)

    def get_by_abbreviation(self, abbreviation: str) -> Currency:
        return self.model.objects.filter(abbreviation=abbreviation).first()

    def update(self, data: dict) -> models.Model:
        abbreviation = data.pop("abbreviation")
        self.model.objects.update_or_create(
            abbreviation=abbreviation,
            defaults={**data}
        )

    def update_many(self, datas: list[dict]) -> None:
        with transaction.atomic(durable=True):
            for obj in datas:
                self.update(obj)
    
    

class RateRepository(ModelRepository):
    model = Rate

    def create_many(self, datas: list[dict]) -> None:
        for obj in datas:
            currency_abbreviation = obj.pop("currency_abbreviation")
            currency = Currency.objects.filter(abbreviation=currency_abbreviation).first()
            obj["currency_abbreviation"] = currency
        save_data = [
            self.model(**data) for data in datas
        ]
        self.model.objects.bulk_create(save_data)
    
    def get(self, _filters: dict) -> Rate:
        result = self.model.objects.filter(**_filters).latest("date")
        return result