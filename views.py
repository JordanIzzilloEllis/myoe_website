from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Employee

# Create your views here.
def index(request):
    return render(request, 'payroll/index.html', {})

def search(request, get_id):
    """
    ID_query = request.GET.get("ID")

    dep_query = request.GET.get("Department")
    type_query = request.GET.get("Type")
    """
    #name_query = request.GET("Name")
    data_base = Employee.objects.all()
    count = 0
    for data in data_base:
        count += 1

    selected_employee = Employee.objects.filter(pk=int(get_id))
    for data in selected_employee:
        name = data.employee_name
        dep = data.employee_dep
        type = data.type

    if int(get_id) > count:
        return HttpResponse('<h1>Sorry bro but your too ugly for me!!!</h1>')

    else:
        return render(request, 'payroll/employeeDetails.html', {'content':[name, dep, type]})
    #name = Employee.objects.filter(pk=get_id)

"""
    if len(name) != 0:
        return HttpResponse(name)

    else:
        return HttpResponse("<h1>cannot be found</h1>")


        if Employee.pk == int(id):
            pass

            #return render(request, 'payroll/pleaseWorkOrJrodanNeverFeelsTrueLove.html', {})
    """

#def index(request):
#return HttpResponse("<h1>PAYROLL</h1>")

