from rest_framework import permissions
from accounts.models import Customer, Employee


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, Customer)


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, Employee)


class IsAssignedEmployee(permissions.BasePermission):
    """После того как сотрудник назначил задачу только он может с ней взаимодействовать"""
    def has_object_permission(self, request, view, obj):
        if obj.executor is None:
            return True
        return obj.executor == request.user


class CanViewTask(permissions.BasePermission):
    """Видеть задачу, назначенную сотрудником, могут создавший ее заказчик,
    назначенный сотрудник и сотрудник с правом доступа ко всем задачам"""
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or (obj.executor == request.user) or (obj.customer == request.user):
            return True
        elif obj.executor is None:
            return True


class CanModifyTask(permissions.BasePermission):
    """Выполненную задачу редактировать нельзя"""
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if obj.status == 'DONE':
                return False
        return True