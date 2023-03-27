from django.shortcuts import render, redirect

from petstagram.main.forms.pets import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.main.helpers import get_profile
from petstagram.main.models import Pet


def create_pet(request):
    profile = get_profile()
    if request.method == 'POST':
        create_pet_form = CreatePetForm(request.POST, instance=Pet(user_profile=profile))
        if create_pet_form.is_valid():
            create_pet_form.save()
            return redirect('profile')
    else:
        create_pet_form = CreatePetForm(instance=Pet(user_profile=profile))
    context = {
        'create_pet_form': create_pet_form,
    }
    return render(request, 'pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditPetForm(instance=pet)
    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeletePetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = DeletePetForm(instance=pet)
    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, 'pet_delete.html', context)