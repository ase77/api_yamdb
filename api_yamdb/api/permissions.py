from rest_framework import permissions


class AuthOrReadOnly(permissions.BasePermission):

    def has_object_permission(sel, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class AdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
        )

    def has_object_permission(self, request, obj, view):
        if request.method == 'GET':
            return True
        return request.user.is_superuser
