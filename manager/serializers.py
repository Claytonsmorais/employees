from rest_framework import serializers
from manager.models import Employee,Department
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','id']

class DepartmentSerializer(serializers.ModelSerializer):
    created_by=UserSerializer()
    link = serializers.HyperlinkedIdentityField(view_name='department-detail-api')
    class Meta:
        model = Department
        fields = (
            'department_id',
            'link',
            'department_name',
            'department_abb',
            'is_active',
            'created_at',
            'created_by',
        )

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    created_by = UserSerializer()
    link = serializers.HyperlinkedIdentityField(view_name='employee-detail-api')
    class Meta:
        model = Employee
        fields = (
                'employee_id',
                'link',
                'employee_first_name',
                'employee_last_name',
                'employee_email',
                'department',
                'is_active',
                'created_at',
                'created_by',)



class EmployeeSerializerPost(serializers.ModelSerializer):
    created_by=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    department=serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    employee_first_name = serializers.SerializerMethodField()
    employee_last_name = serializers.SerializerMethodField()
    employee_email = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = (
                'employee_id',
                'employee_first_name',
                'employee_last_name',
                'employee_email',
                'department',
                'created_by'
            )
    def get_employee_first_name(self,obj):
        return obj.employee_first_name.upper()
    def get_employee_last_name(self,obj):
        return obj.employee_last_name.upper()
    def get_employee_email(self,obj):
        return obj.employee_email.upper()


class DepartmentSerializerPost(serializers.ModelSerializer):
    created_by=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Department
        fields = (
            'department_id',
            'department_name',
            'department_abb',
            'created_by'
        )