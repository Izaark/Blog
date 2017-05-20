
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	message = 'Debes ser propietario de este objeto para realizar esta acción'
	my_safe_method = ['GET','PUT']
	def has_permission(self, request,view):
		if request.method in self.my_safe_method:
			return True
		return False
	def has_object_permission(self, request, view, obj):
		return obj.user == request.user



# class IsOwnerOrReadOnly(permissions.BasePermission):
# 	message = 'Debes ser propietario de este objeto.'
# 	my_safe_method = ['GET','PUT']
# 	def has_permission(self, request,view):
# 		if request.method in self.my_safe_method:
# 			return True
# 		return False

# 	def has_object_permission(self, request, view, obj):

# 		if request.method in permissions.SAFE_METHODS:
# 			return True
# 		return obj.user == request.user