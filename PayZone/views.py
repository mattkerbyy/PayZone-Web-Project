from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Department
from .forms import DepartmentForm

def home(request):
    return render(request, 'home_page/home_web.html')


def user_register(request):
    if request.method == 'POST':
        print('request post')
        form = UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print('form is valid')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('PayZone:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('PayZone:dashboard')  # Redirect to the dashboard or any other desired page
            else:
                messages.error(request, 'Invalid login credentials. Please try again.')
        return render(request, 'user_auth/login.html')


def dashboard(request):
    return render(request, 'main_page/home_dashboard.html')

def employees(request):
    return render(request, 'main_page/employees.html')
def payroll(request):
    return render(request, 'main_page/payroll.html')

def reports(request):
    return render(request, 'main_page/reports.html')

def custom_logout(request):
    logout(request)
    return redirect('home')


def departments(request):
    departments = Department.objects.all()  # Fetch all Department objects
    return render(request, 'main_page/departments.html', {'departments': departments})


def department_list(request):
    departments = Department.objects.all()
    department_form = DepartmentForm()
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST)
        if department_form.is_valid():
            department_form.save()
            return redirect('PayZone:department_list')

    return render(request, 'main_page/departments.html', {'departments': departments, 'department_form': department_form})


def create_department(request):
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST)
        if department_form.is_valid():
            department_form.save()
            return redirect('PayZone:department_list')
    else:
        department_form = DepartmentForm()

    return render(request, 'main_page/departments.html', {'department_form': department_form})


def update_department(request, department_id):
    department = Department.objects.get(id=department_id)
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST, instance=department)
        if department_form.is_valid():
            department_form.save()
            return redirect('PayZone:department_list')

    return redirect('PayZone:department_list')


def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)
    if request.method == 'POST':
        department.delete()

    return redirect('PayZone:department_list')

# def logout(request):
#     # Logout the user
#     auth_logout(request)
#     # Redirect to the home page or any other desired page after logout
#     return redirect('PayZone:logout')
