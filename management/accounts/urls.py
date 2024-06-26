from django.urls import path, include
from .views import (
    CustomerAPIView, EmployeeAPIView, CustomerCreateAPIView, EmployeeCreateAPIView, CurrentUserAPIView
)

app_name = "accounts"

urlpatterns = [
    path('api/v1/customers_list', CustomerAPIView.as_view(), name='customers-list'),
    path('api/v1/employees_list', EmployeeAPIView.as_view(), name='employees-list'),
    path('api/v1/create_customer', CustomerCreateAPIView.as_view(), name='create-customer'),
    path('api/v1/create_employee', EmployeeCreateAPIView.as_view(), name='create-employee'),
    path('api/v1/current_user/', CurrentUserAPIView.as_view(), name='current-user'),
]
