from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from employees_app.employees.views import home, department, department_details, list_departments, redirect_to_home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='home'),
                  path('employees/', include('employees_app.employees.urls')),
                  path('redirect-to-home/', redirect_to_home, name='go to home'),
                  path('templates/', include('employees_app.template_examples.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
