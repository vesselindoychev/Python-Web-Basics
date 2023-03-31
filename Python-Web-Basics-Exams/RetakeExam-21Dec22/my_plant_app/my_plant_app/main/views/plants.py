from django.shortcuts import render, redirect

from my_plant_app.main.forms.plants import CreatePlantForm, EditPlantForm, DeletePlantForm
from my_plant_app.main.models import Plant


def show_create_plant(request):
    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreatePlantForm()

    context = {
        'form': form,
    }

    return render(request, 'create-plant.html', context)


def show_edit_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditPlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'edit-plant.html', context)


def show_delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = DeletePlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'delete-plant.html', context)


def show_details_plant(request, pk):
    plant = Plant.objects.get(pk=pk)

    context = {
        'plant': plant,
    }

    return render(request, 'plant-details.html', context)
