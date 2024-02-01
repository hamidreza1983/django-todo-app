from rest_framework import permissions

class JustAuthenticatedUser(permissions.BasePermission):
    # Just users that are authenticated can see the list and create objects.
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # Just users that are authenticated and the owner of the task can see details and delete objects.
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.user == request.user


        
        