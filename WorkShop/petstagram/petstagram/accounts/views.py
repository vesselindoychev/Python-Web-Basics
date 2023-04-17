from django.contrib.auth import views as auth_views, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.accounts.models import Profile
from petstagram.common.views_mixins import RedirectToDashboard
from petstagram.main.models import Pet, PetPhoto


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('show profile', kwargs={'pk': self.object.pk})


class ChangerUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('password redirect')


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pets = list(Pet.objects.filter(user=self.object.user))
        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
        total_pet_photos_likes = sum(pp.likes for pp in pet_photos)
        total_pet_images = len(pet_photos)

        context.update({
            'total_pet_images': total_pet_images,
            'total_pet_photos_likes': total_pet_photos_likes,
            'pets': pets,
            'is_owner': self.object.user_id == self.request.user.id,
        })

        return context


class DeleteProfileView(views.DeleteView):
    model = Profile
    form_class = DeleteProfileForm
    template_name = 'accounts/profile_delete.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_queryset(self):
        return super().get_queryset()
# def delete_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         delete_profile_form = DeleteProfileForm(request.POST, instance=profile)
#         if delete_profile_form.is_valid():
#             delete_profile_form.save()
#             return redirect('index')
#     else:
#         delete_profile_form = DeleteProfileForm(instance=profile)
#     context = {
#         'delete_profile_form': delete_profile_form,
#     }
#     return render(request, 'main/profile_delete.html', context)
