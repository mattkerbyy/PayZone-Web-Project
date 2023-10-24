from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


app_name = 'PayZone'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('departments/', views.departments, name='departments'),
    path('employees/', views.employees, name='employees'),
    path('payroll/', views.payroll, name='payroll'),
    path('reports/', views.reports, name='reports'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.create_department, name='create_department'),
    path('departments/<int:department_id>/update/', views.update_department, name='update_department'),
    path('departments/<int:department_id>/delete/', views.delete_department, name='delete_department'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/<int:employee_id>/update/', views.update_employee, name='update_employee'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
]