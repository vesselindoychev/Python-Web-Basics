from django.urls import path

from employees_app.template_examples.views import template_home

urlpatterns = (
    path('', template_home, name='templates-index'),
)