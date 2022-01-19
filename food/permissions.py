from rest_framework import permissions, exceptions
from .models import Chef
from .permutils import isChef

class IsChefOrReadOnly(permissions.BasePermission):
    """Cuisine or FoodCategory can be added by the chef but can be read by anyone"""    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated:
            return isChef(request)
        raise exceptions.NotAuthenticated




# class IsSelf(permissions.BasePermission):
#     """
#     Object-level permission to only allow owners of an object to edit it.
#     Assumes the model instance has an `owner` attribute.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         # Instance must have an attribute named `owner`.
#         if hasattr(obj, "owner"):
#             return obj.owner == request.user


