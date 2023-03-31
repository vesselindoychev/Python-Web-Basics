from django.shortcuts import render, redirect

from my_plant_app.main.forms.profiles import CreateProfileForm, EditProfileForm, DeleteProfileForm
from my_plant_app.main.helpers import get_profile
from my_plant_app.main.models import Plant


def show_create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def show_edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def show_delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)


def show_details_profile(request):
    profile = get_profile()
    plants = Plant.objects.all()
    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'profile-details.html', context)