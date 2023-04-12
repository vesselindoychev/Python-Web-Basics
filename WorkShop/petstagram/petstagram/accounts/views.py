from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy


class UserRegisterView:
    pass


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class UserDetailsView:
    pass


class EditProfileView:
    pass


class ChangerUserPasswordView:
    pass
