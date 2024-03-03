from .views import api_get_currencies_view, api_get_rates_view

from django.urls import path


app_name = "currencies"

urlpatterns = [
    path("", api_get_currencies_view, name="list"),
    path("rates/<str:abbreviation>/", api_get_rates_view, name="detail"),
]
