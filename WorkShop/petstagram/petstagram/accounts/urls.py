from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from petstagram.accounts.views import UserLoginView, ProfileDetailsView, UserRegisterView, EditProfileView, \
    ChangerUserPasswordView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),

    # Profiles
    path('create-profile/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='show profile'),
    path('edit-password/<int:pk>/', ChangerUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password redirect'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit-profile'),
    # path('profile/delete/', delete_profile, name='delete-profile'),
]