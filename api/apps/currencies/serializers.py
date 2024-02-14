from rest_framework import serializers

from .models import Currency, Rate


class CustomModelSerializer(serializers.ModelSerializer):
    def create(self, validated_data): ...

    def update(self, instance, validated_data): ...

    def save(self, **kwargs): ...


class CurrencySerializer(CustomModelSerializer):

    class Meta:
        model = Currency
        fields = "__all__"


class RateSerializer(CustomModelSerializer):

    class Meta:
        model = Rate
        fields = "__all__"


class CurrencySerializerWithoutId(CustomModelSerializer):

    class Meta(CurrencySerializer.Meta):
        fields = (
            "abbreviation",
            "name_ru",
            "name_eng",
            "scale",
        )
