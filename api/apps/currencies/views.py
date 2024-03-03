from .repos import CurrencyRepository, BaseRepository, RateRepository
from .models import Currency, Rate
from .serializers import CurrencySerializerWithoutId, RateViewSerializer

from datetime import date

from django.db.models import QuerySet
from django.http import HttpRequest
from rest_framework.views import APIView, Response, status
from rest_framework.serializers import BaseSerializer


class CurrencyView(APIView):

    def __init__(
        self,
        repository: BaseRepository = CurrencyRepository,
        serializer: BaseSerializer = CurrencySerializerWithoutId,
        **kwargs
    ) -> None:
        self._repository = repository
        self._serializer = serializer
        super().__init__(**kwargs)

    def get(self, request: HttpRequest, *args, **kwargs) -> Response:
        currencies: QuerySet[Currency] = self._repository().get_all()
        serialize = self._serializer(instance=currencies, many=True)
        return Response(data=serialize.data, status=status.HTTP_200_OK)



api_get_currencies_view = CurrencyView.as_view()


class RateView(APIView):
    
    def __init__(
            self,
            repository: BaseRepository = RateRepository,
            serializer: BaseSerializer = RateViewSerializer,
            **kwargs
    ) -> None:
        self._repository = repository
        self._serializer = serializer
        super().__init__(**kwargs)
    
    def get(self, request: HttpRequest, *args, **kwargs):
        abbreviation = kwargs.get("abbreviation")
        if abbreviation:
            rate: Rate = self._repository().get({"currency_abbreviation": abbreviation, "date": date.today()})
            serialize = self._serializer(instance=rate)
            return Response(data=serialize.data, status=status.HTTP_200_OK)
    

api_get_rates_view = RateView.as_view()