from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #SAFE_METHODS are GET Request or POST
            return True

        return obj.id == request.user.id #Return True jika ID login = id profile
