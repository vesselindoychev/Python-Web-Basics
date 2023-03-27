from django.shortcuts import render, redirect

from petstagram.main.forms.profiles import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto, Pet


def show_profile(request):
    profile = get_profile()
    # if not profile:
    #     return render(request, '401_error.html')
    pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct()
    total_pet_photos_likes = sum(pp.likes for pp in pet_photos)
    total_pet_images = len(pet_photos)
    pets = Pet.objects.filter(user_profile=profile)
    context = {
        'profile': profile,
        'total_pet_images': total_pet_images,
        'total_pet_photos_likes': total_pet_photos_likes,
        'pets': pets,
    }
    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        create_profile_form = CreateProfileForm(request.POST, request.FILES)

        if create_profile_form.is_valid():
            create_profile_form.save()
            return redirect('index')
    else:
        create_profile_form = CreateProfileForm()

    context = {
        'create_profile_form': create_profile_form,
    }
    return render(request, 'profile_create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return redirect('profile')
    else:
        edit_profile_form = EditProfileForm(instance=profile)

    context = {
        'edit_profile_form': edit_profile_form,
    }

    return render(request, 'profile_edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        delete_profile_form = DeleteProfileForm(request.POST, instance=profile)
        if delete_profile_form.is_valid():
            delete_profile_form.save()
            return redirect('index')
    else:
        delete_profile_form = DeleteProfileForm(instance=profile)
    context = {
        'delete_profile_form': delete_profile_form,
    }
    return render(request, 'profile_delete.html', context)