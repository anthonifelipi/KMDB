from rest_framework import permissions
from rest_framework.views import Request, View


class AcessReviews(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_critic or request.user.is_superuser


class DeleteReview(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, review):

        if request.method in permissions.SAFE_METHODS:
            return True

        if review[0].user.id == request.user.id:
            return True

        return request.user.is_superuser
