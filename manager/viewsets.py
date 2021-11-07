from manager.serializers import EmployeeSerializer,DepartmentSerializer,EmployeeSerializerPost,DepartmentSerializerPost
from rest_framework.views import APIView
from manager.models import Employee,Department
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from manager.permissions import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.reverse import reverse
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

class APIRootView(APIView):
    def get(self, request):
        data = {
            'employees-api': reverse('employees-api', request=request),
            'departments-api': reverse('departments-api', request=request),
            'jwt-login': reverse('jwt-login', request=request),
            'jwt-refresh': reverse('jwt-refresh', request=request),
            'search-employee': reverse('search-employee',args=['term'], request=request),
        }
        return Response(data)

class EmployeeSearchViewSet(APIView):
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]
    permission_classes = [EmployeePermission]
    def get(self,request,term):
        paginator = PageNumberPagination()
        data = Employee.objects.filter(
            Q(employee_first_name__icontains=term)
            |
            Q(employee_last_name__icontains=term)
        )
        result_page = paginator.paginate_queryset(data, request)
        serial_data = EmployeeSerializer(result_page,many=True,context={'request': request})
        return paginator.get_paginated_response(serial_data.data)


class EmployeeViewSet(APIView):
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]
    permission_classes = [EmployeePermission]


    def get(self,request):
        data = Employee.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(data, request)
        serial_data = EmployeeSerializer(result_page,many=True,context={'request': request})
        return paginator.get_paginated_response(serial_data.data)

    def post(self,request):
        if 'employee_email' in request.data:
            if Employee.objects.filter(employee_email__iexact=request.data['employee_email']):
                return Response({'Employee email already registered'},status=status.HTTP_400_BAD_REQUEST)

        request.data['created_by']=request.user.id
        serializer = EmployeeSerializerPost(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class DepartmentViewSet(APIView):
    permission_classes = [DepartmentPermission]
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]
    def get(self,request):
        data = Department.objects.all()
        paginator = PageNumberPagination()
        page_result = paginator.paginate_queryset(data,request)
        serial_data = DepartmentSerializer(page_result,many=True,context={'request': request})
        return paginator.get_paginated_response(serial_data.data)

    def post(self,request):
        if 'department_abb' in request.data:
            if Department.objects.filter(department_abb__iexact=request.data['department_abb']):
                return Response({'Department abbreviation already registered'},status=status.HTTP_400_BAD_REQUEST)

        request.data['created_by']=request.user.id
        serializer = DepartmentSerializerPost(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class DepartmentDetailViewSet(APIView):
    permission_classes = [DepartmentPermission]
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]
    def get(self,request,pk):
        data = get_object_or_404(pk=pk,klass=Department)
        serial_data = DepartmentSerializer(data,context={'request': request})
        return Response(serial_data.data)

class EmployeeDetailViewSet(APIView):
    permission_classes = [EmployeePermission]
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]
    def get(self,request,pk):
        data = get_object_or_404(pk=pk,klass=Employee)
        serial_data = EmployeeSerializer(data,context={'request': request})
        return Response(serial_data.data)
    def delete(self,request,pk):
        obj = get_object_or_404(Employee,pk=pk)
        obj.delete()
        return Response('Object deleted gracefully', status=status.HTTP_200_OK)


