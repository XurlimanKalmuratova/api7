from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method == 'POST':
            return request.user.is_authenticated


class UserDetailPermission(BasePermission):
    def has_permisson(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_staff
        


class TaskPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method ==  'GET':
            return request.user.is_authenticated
        elif request.method == 'POST':
            return request.user.is_authenticated


class TaskDetailPermission(BasePermission):
    def has_permisson(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_authenticated




class ProjectPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated


class ProjectDetailPermission(BasePermission):
    def has_permisson(self, request, view):
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated