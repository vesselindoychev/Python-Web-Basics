from django.contrib import admin
from django.urls import path, include

from employees_app.employees.views import home, department, department_details, list_departments, redirect_to_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('departments/', include('employees_app.employees.urls')),
    path('redirect-to-home/', redirect_to_home, name='go to home'),
]