from django.contrib import admin
from .models import Employee, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'department', 'hire_date', 'salary', 'email', 'phone_number')
    list_filter = ('gender', 'department', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')