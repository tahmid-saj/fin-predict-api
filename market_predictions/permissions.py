from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
  
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      return bool(request.user and request.user.is_staff)

class AdminOnly(permissions.IsAdminUser):
  
  def has_permission(self, request, view):
    return bool(request.user and request.user.is_staff)