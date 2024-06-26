from .models import Customer, Employee
from .serializers import (
    UserCreateSerializer, CustomerSerializer, EmployeeSerializer, EmployeeCreateSerializer, UserSerializer, CustomerCreateSerializer
)
from rest_framework.response import Response
from rest_framework import generics, permissions
from main.permissions import IsEmployee, IsCustomer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class CustomerAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsEmployee]


class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permissions_classes = [IsCustomer]


class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer
    permission_classes = [IsEmployee]


class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerializer
    permission_classes = [IsCustomer]


class CurrentUserAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserCreateSerializer(user, context=self.get_serializer_context()).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=400)