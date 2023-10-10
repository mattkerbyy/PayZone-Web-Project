from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"