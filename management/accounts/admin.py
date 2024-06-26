from django.contrib import admin

# Register your models here.
from .models import Customer, Employee


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'phone']
    raw_id_fields = ['user']
    search_fields = ('surname', 'name', 'patronymic', 'phone')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'phone']
    raw_id_fields = ['user']
    search_fields = ('surname', 'name', 'patronymic', 'phone')
    list_filter = ('company', 'job_title')


