from django.urls import path

from .views import HealthCheckView

app_name = "core"

urlpatterns = [path("ping/", HealthCheckView.as_view())]
