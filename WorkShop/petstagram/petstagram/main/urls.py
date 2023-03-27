from django.urls import path

from petstagram.main.views.generic import show_home, show_dashboard
from petstagram.main.views.pet_photos import create_pet_photo, edit_pet_photo, show_pet_photo_details, like_pet_photo, \
    delete_pet_photo
from petstagram.main.views.pets import create_pet, edit_pet, delete_pet
from petstagram.main.views.profiles import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = [

    # Home
    path('', show_home, name='index'),

    # Dashboard
    path('dashboard/', show_dashboard, name='dashboard'),

    # Profiles
    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create-profile'),
    path('profile/edit/', edit_profile, name='edit-profile'),
    path('profile/delete/', delete_profile, name='delete-profile'),

    # Pets
    path('pet/add/', create_pet, name='create-pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit-pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete-pet'),


    # Pet Photos
    path('photo/add/', create_pet_photo, name='create-pet-photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit-pet-photo'),
    path('photo/delete/<int:pk>/', delete_pet_photo, name='delete-pet-photo'),
    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet-photo-details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like-pet-photo'),

]