from django.urls import path

from expenses_tracker.main.views.expenses import show_create_expenses_view, show_edit_expenses_view, \
    show_delete_expenses_view
from expenses_tracker.main.views.general import show_home_with_profile
from expenses_tracker.main.views.profiles import show_profile, show_edit_profile, show_delete_profile, \
    show_create_profile

urlpatterns = [
    # Home
    path('', show_home_with_profile, name='show home with profile'),

    # Expenses
    path('create/', show_create_expenses_view, name='create expense view'),
    path('edit/<int:pk>/', show_edit_expenses_view, name='edit expense view'),
    path('delete/<int:pk>/', show_delete_expenses_view, name='delete expense view'),

    # Profiles
    path('profile/', show_profile, name='profile page'),
    path('profile/create/', show_create_profile, name='create profile page'),
    path('profile/edit/', show_edit_profile, name='edit profile page'),
    path('profile/delete/', show_delete_profile, name='delete profile page'),
]
