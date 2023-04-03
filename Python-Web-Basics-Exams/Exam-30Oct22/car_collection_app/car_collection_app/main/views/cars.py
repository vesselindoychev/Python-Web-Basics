from django.shortcuts import render, redirect

from car_collection_app.main.forms.cars import CreateCarForm, EditCarForm, DeleteCarForm
from car_collection_app.main.models import Car


def create_car(request):
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateCarForm()

    context = {
        'form': form,
    }

    return render(request, 'car-create.html', context)


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditCarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditCarForm(instance=car)

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = DeleteCarForm(instance=car)

    context = {
        'car':car,
        'form': form,
    }

    return render(request, 'car-delete.html', context)


def details_car(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car': car,
    }
    return render(request, 'car-details.html', context)
