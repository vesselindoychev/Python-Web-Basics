from django.urls import path

from employees_app.employees.views import department_details, department, list_departments, create_employee, \
    edit_employee

urlpatterns = [
    path('', department),
    path('details/<id>/', department_details),
    path('list/', list_departments, name='list-departments'),
    path('create/', create_employee, name='create-employee'),
    path('edit/<int:pk>/', edit_employee, name='edit-employee'),
]
