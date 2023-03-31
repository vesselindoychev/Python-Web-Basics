from django.urls import path

from my_plant_app.main.views.general import show_home, show_catalogue
from my_plant_app.main.views.plants import show_create_plant, show_details_plant, show_edit_plant, show_delete_plant
from my_plant_app.main.views.profiles import show_create_profile, show_edit_profile, show_delete_profile, \
    show_details_profile

urlpatterns = [
    # Home
    path('', show_home, name='home'),
    path('catalogue/', show_catalogue, name='catalogue'),

    # Profiles
    path('profile/create/', show_create_profile, name='create profile'),
    path('profile/edit/', show_edit_profile, name='edit profile'),
    path('profile/delete/', show_delete_profile, name='delete profile'),
    path('profile/details/', show_details_profile, name='details profile'),

    # Plants
    path('create/', show_create_plant, name='create plant'),
    path('details/<int:pk>/', show_details_plant, name='details plant'),
    path('edit/<int:pk>/', show_edit_plant, name='edit plant'),
    path('delete/<int:pk>/', show_delete_plant, name='delete plant'),
]