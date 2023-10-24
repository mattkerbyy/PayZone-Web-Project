from django import forms
from .models import Department
from .models import Employee


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'department', 'hire_date', 'salary', 'email', 'phone_number', 'address']
