import random

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from employees_app.employees.models import Department, Employee


def home(request):
    number = 69

    context = {
        'number': number,
        'numbers': [random.randint(0, 1024) for _ in range(7)]
    }
    return render(request, 'index.html', context)
    # return HttpResponse('This is home')


def redirect_to_home(request):
    return redirect('home')


def department(request):
    return HttpResponse('This is department')


def department_details(request, id):
    return HttpResponse(f'This is department details {id}')


def list_departments(request):
    context = {
        'departments': Department.objects.prefetch_related('employee_set').all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)