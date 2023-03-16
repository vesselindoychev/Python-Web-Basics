from django.urls import path

from employees_app.employees.views import department_details, department, list_departments

urlpatterns = [
    path('', department),
    path('details/<id>/', department_details),
    path('list/', list_departments, name='list-departments'),
]
