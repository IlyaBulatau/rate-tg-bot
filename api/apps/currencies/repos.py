from abc import ABC, abstractmethod

from django.db import models

from api.services.domains import CurrencyDomain, RateDomain
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
    def get(self) -> models.Model:
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
    
    def get(self) -> models.Model:
        ...
    
    def delete(self) -> None:
        ...


class CurrencyRepository(ModelRepository):
    model = Currency

class RateRepository(ModelRepository):
    model = Rate

