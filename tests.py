from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from random import choice
from manager.models import Employee,Department

class EmployeeTestCase(APITestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.superuser = User.objects.create_superuser('clayton', 'john@snow.com', '123456')
        self.client.login(username='clayton', password='123456')
        self.data = {
                    "employee_first_name":"John",
                    "employee_last_name":"Travolta",
                    "department":choice(Department.objects.all()).department_id,
                    "employee_email":"john_travolt@employee.com"
                }
    def test_addNewEmployee(self):
        response = self.client.post(reverse('employees-api'),self.data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    def test_DeleteEmployee(self):
        response = self.client.delete(reverse('employee-detail-api',args=[choice(Employee.objects.all()).employee_id]))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_retrieveEmployees(self):
        response = self.client.get(reverse('employees-api'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_searchEmployee(self):
        response = self.client.get(reverse('search-employee',args=['cl']))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_detailEmployee(self):
        response = self.client.get(reverse('employee-detail-api',args=[choice(Employee.objects.all()).employee_id]))
        self.assertEqual(response.status_code,status.HTTP_200_OK)



class DepartmentTestCase(APITestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.superuser = User.objects.create_superuser('clayton', 'john@snow.com', '123456')
        self.client.login(username='clayton', password='123456')
        self.data = {
                        "department_name":"TEST",
                        "department_abb":"TST"
                    }
    def test_addNewDepartent(self):
        response = self.client.post(reverse('departments-api'),self.data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    def test_retrieveDepartments(self):
        response = self.client.get(reverse('departments-api'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_detailDepartment(self):
        response = self.client.get(reverse('department-detail-api',args=[choice(Department.objects.all()).department_id]))
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class JWTTesCase(APITestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.superuser = User.objects.create_superuser('clayton', 'john@snow.com', '123456')
        self.data = {
            "username": "clayton",
            "password": "123456"
        }
        response = self.client.post(reverse('jwt-login'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='JWT {}'.format(self.token))

    def test_reqToken(self):
        response=self.client.get(reverse('employees-api'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_refreshToken(self):
        response=self.client.post(reverse('jwt-refresh'),data={'token':self.token},format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)





