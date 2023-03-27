from django.shortcuts import render

from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto


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