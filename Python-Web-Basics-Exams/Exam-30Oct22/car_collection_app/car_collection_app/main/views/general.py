from django.shortcuts import render

from car_collection_app.main.models import Car


def show_home(request):
    return render(request, 'index.html')


def show_catalogue(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
    }
    return render(request, 'catalogue.html', context)
