from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'customer', 'executor', 'closing_date']
    search_fields = ('title', 'update_date', 'date_of_creation', 'closing_date')
    list_filter = ('status',)
    date_hierarchy = 'closing_date'
