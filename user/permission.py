from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None

# def is_in_admin_group(user, g)

# class HasGroupPermission(permissions.BasePermission):
#     """
#     Ensure user is in required groups.
#     """
#
#     def has_permission(self, request, view):
#         required_groups = view.permission_groups.get(view.action)
#         if required_groups is None:
#             return False
#         return any([is_in_group(request.user, group_name) for group_name in required_groups])
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         if request.method == 'DELETE':
#             return True
#         return obj.id == request.user.id


def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])


class IsLoggedInUserOrSuperAdmin(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        if self.required_groups is None:
            return False
        return obj == request.user or has_group_permission


class IsAdminUser(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class IsAdminOrAnonymousUser(permissions.BasePermission):
    required_groups = ['admin', 'anonymous']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission
