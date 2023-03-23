import random

from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django import forms
from employees_app.employees.models import Department, Employee


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be positive!')


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Enter First Name',
#             },
#         ),
#
#     )
#
#     last_name = forms.CharField(
#         max_length=40,
#     )
#
#     egn = forms.CharField(
#         max_length=10,
#     )
#
#     age = forms.IntegerField(
#         validators=(
#             validate_positive,
#         )
#     )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             (j, j) for j in Employee.JOB_TITLES
#         ),
#     )
#
#     company = forms.ChoiceField(
#         choices=((c, c) for c in Employee.COMPANIES),
#     )


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter first name'},
            ),
            'egn': forms.TextInput(
                attrs={'placeholder': '0000000000'},
            )
        }


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First name'),
            ('last_name', 'Last name'),
            ('job_title', 'Job title'),
        ),
    )


class EditEmployeeForm(EmployeeForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={'readonly': 'readonly'}
            )
        }


def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            # emp = Employee(
            #     **employee_form.cleaned_data,
            #     department_id=1,
            # )
            # emp.save()
            # return redirect('home')
            employee_form.save()
            return redirect('home')
    else:
        employee_form = EmployeeForm()
    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }
    return render(request, 'employees/create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        employee_form = EditEmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create-employee')
    else:
        employee_form = EditEmployeeForm(request.FILES, instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form,
    }
    return render(request, 'employees/edit.html', context)


def home(request):
    number = 69

    context = {
        'number': number,
        'numbers': [random.randint(0, 1024) for _ in range(7)],
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
