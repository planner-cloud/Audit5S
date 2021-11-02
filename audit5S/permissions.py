from rest_framework import permissions

class OnlyAdminPermission(permissions.BasePermission):
    message = 'Only Admin are allowed to create or modify zones.'

    def has_permission(self, request, view):
        return request.user.is_admin or request.user.is_superuser