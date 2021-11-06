from rest_framework.permissions import BasePermission

class DepartmentPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method.upper() =='GET':
            if request.user.has_perm("manager.view_department"):
                return True
            else:
                return False
        elif request.method.upper() == 'POST':
            if request.user.has_perm("manager.add_department"):
                return True
            else:
                return False


class EmployeePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method.upper() =='GET':
            if request.user.has_perm("manager.view_employee"):
                return True
            else:
                return False
        elif request.method.upper() == 'POST':
            if request.user.has_perm("manager.add_employee"):
                return True
            else:
                return False
        elif request.method.upper() == 'DELETE':
            if request.user.has_perm("manager.delete_employee"):
                return True
            else:
                return False


