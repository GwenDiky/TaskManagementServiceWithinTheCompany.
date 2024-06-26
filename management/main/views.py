from rest_framework import generics, permissions
from accounts.serializers import CustomerSerializer, EmployeeSerializer
from .serializers import TaskSerializer, TaskAssignSerializer
from .models import Task
from .permissions import IsCustomer, CanViewTask, IsAssignedEmployee, CanModifyTask
from accounts.models import Customer


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsCustomer]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.person)


class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAssignSerializer
    permission_classes = [IsAssignedEmployee, permissions.IsAuthenticated, CanModifyTask]

    def perform_update(self, serializer):
        serializer.save(executor=self.request.user.employee)


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'person') and isinstance(user.person, Customer):
            return Task.objects.filter(customer=user.person)
        else:
            return Task.objects.all()


class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [CanViewTask]