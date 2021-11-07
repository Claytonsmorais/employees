import os
import django
os.environ['DJANGO_SETTINGS_MODULE']='employees.settings.development'
django.setup()
from random import choice
from faker import Faker

import factory
from manager.models import Employee,Department
from django.contrib.auth.models import User
class EmployeeFactory(factory.Factory):
    class Meta:
        model = Employee

    employee_first_name=factory.Faker('first_name')
    employee_last_name=factory.Faker('last_name')
    employee_email=factory.LazyAttribute(lambda o: '{}.{}@employees.com'.format(o.employee_first_name.lower(),o.employee_last_name.lower()))
    department=factory.Iterator(Department.objects.all())
    created_by=factory.Iterator(User.objects.all())

for x in range(1000):
    nObj = EmployeeFactory()
    nObj.save()
