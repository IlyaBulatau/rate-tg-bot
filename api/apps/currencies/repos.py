from abc import ABC, abstractmethod

from django.db import models
from rest_framework.serializers import ModelSerializer

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
    
    def __init__(self, model: models.Model | None):
        if model:
            self.model = model

    def create(self, serializer: ModelSerializer) -> models.Model:
        obj = self.model.objects.create(**serializer.data)
        return obj
    
    def update(self) -> models.Model:
        ...
    
    def get(self) -> models.Model:
        ...
    
    def delete(self) -> None:
        ...


class BaseCurrencyRepository(ModelRepository):
    model = Currency

class BaseRateRepository(ModelRepository):
    model = Rate

