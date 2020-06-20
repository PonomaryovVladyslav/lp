from rest_framework import permissions

from hopital.models import Doctor


class OnlyDoctor(permissions.BasePermission):

    def has_permission(self, request, view):
        return hasattr(request.user, 'doctor')
