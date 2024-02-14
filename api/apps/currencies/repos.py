from abc import ABC, abstractmethod

from django.db import models

from services.domains import CurrencyDomain, RateDomain
from .models import Currency, Rate


class BaseRepository(ABC):
    model = None

    @abstractmethod
    def create(self) -> models.Model:
        ...
    
    @abstractmethod
    def update(self) -> models.Model:
        ...
    
    @abstractmethod
    def get_all(self) -> models.Model:
        ...
    
    @abstractmethod
    def delete(self) -> None:
        ...
    
class ModelRepository(BaseRepository):
    
    def __init__(self, model: models.Model | None = None):
        if model:
            self.model = model

    def create(self, data: dict) -> models.Model:
        obj = self.model.objects.create(**data)
        return obj

    def create_many(self, datas: list[dict]) -> None:
        self.model.objects.bulk_create([self.model(**data) for data in datas])
    
    def update(self) -> models.Model:
        ...
    
    def get_all(self) -> models.QuerySet[models.Model]:
        return self.model.objects.all()
    
    def delete(self) -> None:
        ...


class CurrencyRepository(ModelRepository):
    model = Currency

    def get_all(self) -> models.QuerySet[models.Model]:
        return self.model.objects.only("abbreviation", "name_ru", "name_eng", "scale").all()

    def get_currencies_abbr(self) -> list[str]:
        result = self.model.objects.values_list("abbreviation", flat=True)
        return list(result)

    def get_by_abbreviation(self, abbreviation: str) -> Currency:
        return self.model.objects.filter(abbreviation=abbreviation).first()

class RateRepository(ModelRepository):
    model = Rate

    def create_many(self, datas: list[tuple[Currency, dict]]) -> None:
        save_data = [
            self.model(
                currency_abbreviation=data[0],
                **data[1]
            ) for data in datas
            ]
        self.model.objects.bulk_create(save_data)

    