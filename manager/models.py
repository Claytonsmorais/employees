from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=5000,null=False,blank=False)
    department_abb= models.CharField(max_length=10,null=False,blank=False,unique=True)
    is_active = models.BooleanField(null=False,default=True)
    created_at = models.DateTimeField(null=False,auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    def __str__(self):
        return '{} - {} '.format(self.department_abb,self.department_name)

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_first_name = models.CharField(max_length=1000,null=False,blank=False)
    employee_last_name = models.CharField(max_length=2000, null = False,blank=False)
    employee_email = models.EmailField(max_length=5000, null=True, blank=False,unique=True)
    department= models.ForeignKey(
        Department,on_delete=models.DO_NOTHING
    )
    is_active = models.BooleanField(null=False,default=True)
    created_at = models.DateTimeField(null=False,auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    def __str__(self):
        return '{} {} ({})'.format(self.employee_first_name,self.employee_last_name,self.department.department_abb)