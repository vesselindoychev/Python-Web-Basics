from django.urls import path

from car_collection_app.main.views.cars import create_car, edit_car, delete_car, details_car
from car_collection_app.main.views.general import show_home, show_catalogue
from car_collection_app.main.views.profiles import create_profile, edit_profile, delete_profile, show_profile

urlpatterns = [
    # HOME
    path('', show_home, name='home'),

    # CATALOGUE
    path('catalogue/', show_catalogue, name='catalogue'),

    # PROFILES
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/details/', show_profile, name='show profile'),

    # CARS
    path('car/create/', create_car, name='create car'),
    path('car/<int:pk>/edit/', edit_car, name='edit car'),
    path('car/<int:pk>/delete/', delete_car, name='delete car'),
    path('car/<int:pk>/details/', details_car, name='details car'),

]