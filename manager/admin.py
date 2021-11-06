from django.contrib import admin
from manager.models import Department,Employee

class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','created_by',)
    def save_model(self, request, obj, form, change):
        if obj.created_by_id is None:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','created_by',)

    def save_model(self, request, obj, form, change):
        if obj.created_by_id is None:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)