from django.shortcuts import render, redirect

from petstagram.main.models import Profile, PetPhoto


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pets = profile.pet_set.all()
    pet_photos = set(PetPhoto.objects.filter(tagged_pets__user_profile=profile))
    context = {
        'pets': pets,
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


def show_profile(request):
    return render(request, 'profile_details.html')


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)

    context = {
        'pet_photo': pet_photo,
    }

    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet-photo-details', pk)