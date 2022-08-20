from rest_framework import permissions
from rest_framework.views import Request, View


class AcessAllOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser


class AcessOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user):

        if user.id == request.user.id or request.user.is_superuser:
            return True
