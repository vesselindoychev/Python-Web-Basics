from django.shortcuts import render, redirect

from car_collection_app.main.forms.profiles import CreateProfileForm, EditProfileForm, DeleteProfileForm
from car_collection_app.main.models import Profile, Car


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateProfileForm(request.FILES)

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
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

    return render(request, 'profile-delete.html', context)


def show_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_price = sum([car.price for car in cars])

    context = {
        'profile': profile,
        'total_price': total_price,
    }
    return render(request, 'profile-details.html', context)
