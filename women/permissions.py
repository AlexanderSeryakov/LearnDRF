from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Разрешает безопасные методы для всех пользователей, а иные методы лишь для пользователя,
    который связан с просматриваемой записью таблицы"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешает безопасные методы для всех пользователей, а иные методы лишь для администратора (superuser)"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser

