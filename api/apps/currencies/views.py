from .repos import CurrencyRepository, BaseRepository
from .models import Currency
from .serializers import CurrencySerializerWithoutId

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
