from django.contrib import admin
from django.urls import path, include
from .views import TaskUpdateAPIView, TaskCreateAPIView, TaskDetailAPIView, TaskListAPIView

app_name = "main"

urlpatterns = [
    path('api/v1/tasks', TaskListAPIView.as_view(), name='tasks'),
    path('api/v1/tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('api/v1/tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('api/v1/tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
]


admin.site.header = "Сервис по управлению задачами внутри компаний"
admin.site.site_title = "Manager"
admin.site.index_title = "Добро пожаловать в сервис по управлению задачами внутри компаний"