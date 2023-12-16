"""API custom permissions."""
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Custom class for accessing Post and Comment objects.

    Set permissions for save methods for everyone.
    And author of the object for other permissions.
    """

    def has_object_permission(self, request, view, obj):
        """Object permission."""
        return (
            request.user.is_authenticated and (
                request.method in SAFE_METHODS or obj.author == request.user
            )
        )
