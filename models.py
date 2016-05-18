from django.db import models

# Create your models here.
class Employee_type(models.Model):
    type_of_employee = models.CharField(max_length=250)

    def __str__(self):
        return self.type_of_employee

class Employee_department(models.Model):
    department = models.CharField(max_length=250)

    def __str__(self):
        return self.department

class Employee(models.Model):
    type = models.ForeignKey(Employee_type, on_delete=models.CASCADE)
    employee_dep = models.ForeignKey(Employee_department, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=250)

    def __str__(self):
        return self.employee_name + " - " + str(self.type) + " - " + str(self.employee_dep)

    def get_name(self):
        return self.employee_name