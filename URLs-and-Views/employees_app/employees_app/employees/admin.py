from django.contrib import admin

from employees_app.employees.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job_title', 'company', 'department')
    # ordering = ('first_name', )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


