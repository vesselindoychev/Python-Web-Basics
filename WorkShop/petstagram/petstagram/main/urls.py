from django.urls import path

from petstagram.main.views.generic import HomeView, DashboardView
from petstagram.main.views.pet_photos import like_pet_photo, \
    delete_pet_photo, CreatePetPhotoView, PetPhotoDetailsView, EditPetPhotoView, DeletePetPhotoView
from petstagram.main.views.pets import CreatePetView, EditPetView, DeletePetView


urlpatterns = [

    # Home
    path('', HomeView.as_view(), name='index'),

    # Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Pets
    path('pet/add/', CreatePetView.as_view(), name='create-pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit-pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete-pet'),


    # Pet Photos
    path('photo/add/', CreatePetPhotoView.as_view(), name='create-pet-photo'),
    path('photo/edit/<int:pk>/', EditPetPhotoView.as_view(), name='edit-pet-photo'),
    path('photo/delete/<int:pk>/', DeletePetPhotoView.as_view(), name='delete-pet-photo'),
    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet-photo-details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like-pet-photo'),

]