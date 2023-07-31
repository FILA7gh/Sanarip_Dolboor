from rest_framework import permissions


class IsAuthenticatedAndFavoriteProductOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # проверка на авторизованность пользователя
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # возвращаем обьекты пользователя
        return obj.user == request.user
