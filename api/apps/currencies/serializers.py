from rest_framework import serializers

from .models import Currency, Rate


class CustomModelSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        ...
    
    def update(self, instance, validated_data):
        ...
    
    def save(self, **kwargs):
        ...

class CurrencySerializer(CustomModelSerializer):
    
    class Meta:
        moddel = Currency
        fields = "__all__"

class RateSerializer(CustomModelSerializer):

    class Meta:
        model = Rate
        fields = "__all__"