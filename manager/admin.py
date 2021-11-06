from django.contrib import admin
from manager.models import Department,Employee

class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','created_by',)
    def save_model(self, request, obj, form, change):
        if obj.created_by_id is None:
            obj.created_by = request.user
        obj.employee_email=obj.employee_email.upper()
        obj.employee_first_name=obj.employee_first_name.upper()
        obj.employee_last_name=obj.employee_last_name.upper()
        super().save_model(request, obj, form, change)

class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','created_by',)

    def save_model(self, request, obj, form, change):
        if obj.created_by_id is None:
            obj.created_by = request.user
        obj.department_abb =obj.department_abb.upper()
        obj.department_name =obj.department_name.upper()
        super().save_model(request, obj, form, change)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)