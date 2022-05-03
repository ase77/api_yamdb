from rest_framework import permissions


class AuthOrReadOnly(permissions.BasePermission):

    def has_object_permission(sel, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
