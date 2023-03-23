from django.shortcuts import render
from django import forms
from employees_app.employees.models import Employee, Department


def template_home(request):
    context = {
        'title': 'Employees List',
        'employees': Employee.objects.order_by('-first_name', 'last_name').all(),
        'department_names': [d.name for d in Department.objects.all()],
        'number_1': 200,
    }
    return render(request, 'template_examples/index.html', context)
