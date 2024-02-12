from rest_framework.permissions import BasePermission
from django.conf import settings
from django.http import HttpRequest

from apps.utils.utils import AccesTokenFromHeaderService


class HeaderAuthenticatedTokenPermission(BasePermission):

    def has_permission(self, request: HttpRequest, view):
        access_service = AccesTokenFromHeaderService(request.headers)
        if not access_service.is_access(settings.AUTH_TOKEN):
            return False
        return True