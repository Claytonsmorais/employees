"""employees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from manager.viewsets import (EmployeeViewSet,
                              DepartmentDetailViewSet,
                              DepartmentViewSet,
                              EmployeeDetailViewSet,
                              APIRootView,
                              EmployeeSearchViewSet
                              )
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('', APIRootView.as_view()),
    re_path(r'api/employees\/?$', EmployeeViewSet.as_view(),name='employees-api'),
    re_path(r'api/departments/(?P<pk>\d+)\/?$', DepartmentDetailViewSet.as_view(),name='department-detail-api'),
    re_path(r'api/departments\/?$', DepartmentViewSet.as_view(),name='departments-api'),
    re_path(r'api/employees/(?P<pk>\d+)\/?$', EmployeeDetailViewSet.as_view(),name='employee-detail-api'),
    re_path(r'api/login\/?$', obtain_jwt_token,name='jwt-login'),
    re_path(r'api/refresh-token\/?$', refresh_jwt_token,name='jwt-refresh'),
    re_path(r'api/employees/search/(?P<term>\w+)\/?$', EmployeeSearchViewSet.as_view(),name='search-employee'),
]
