from django.shortcuts import render

from my_plant_app.main.models import Plant


def show_home(request):
    return render(request, 'home-page.html')


def show_catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants,
    }

    return render(request, 'catalogue.html', context)
