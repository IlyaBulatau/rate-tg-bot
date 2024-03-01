from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest


class HealthCheckView(APIView):

    def get(self, request: HttpRequest, *args, **kwargs):
        return Response(data="pong")
