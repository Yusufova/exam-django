from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):   # It is used in all methods except Update method
        if request.method in SAFE_METHODS:  # if request does not return 404 (if it is safe),
            return True

        return bool(request.user and request.user.is_staff)



class IsOwnerOrReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        if request.user.username   and  request.method in SAFE_METHODS:
            members = obj.members.filter(user=request.user)
            if len(members):
                return True

