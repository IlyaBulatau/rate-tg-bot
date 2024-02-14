from .views import api_get_currencies_view

from django.urls import path, include


app_name = "currencies"

urlpatterns = [
    path("", api_get_currencies_view, name="list"),
]
