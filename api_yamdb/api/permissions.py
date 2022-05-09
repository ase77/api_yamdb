from rest_framework import permissions

from review.models import UserRole


class AdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == UserRole.ADMIN


class AuthorOrModeratorOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj): 
        if request.user == obj.author:
            return True

        return request.user.role in (UserRole.MODERATOR, UserRole.ADMIN)


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
            or request.user.role == UserRole.ADMIN
        )

    def has_object_permission(self, request, obj, view):
        if request.method == 'GET':
            return True
        return request.user.role == UserRole.ADMIN
