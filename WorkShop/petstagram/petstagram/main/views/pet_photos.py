from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.forms.pet_photos import CreatePetPhotoForm, EditPetPhotoForm, DeletePetPhotoForm

from petstagram.main.models import PetPhoto


class CreatePetPhotoView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = CreatePetPhotoForm
    template_name = 'main/photo_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPetPhotoView(views.UpdateView):
    model = PetPhoto
    form_class = EditPetPhotoForm
    template_name = 'main/photo_edit.html'

    def get_success_url(self):
        return reverse_lazy('pet-photo-details', kwargs={'pk': self.object.id})


# def edit_pet_photo(request, pk):
#     pet_photo = PetPhoto.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EditPetPhotoForm(request.POST, instance=pet_photo)
#         if form.is_valid():
#             form.save()
#             return redirect('pet-photo-details', pet_photo.pk)
#     else:
#         form = EditPetPhotoForm(instance=pet_photo)
#
#     context = {
#         'form': form,
#         'pet_photo': pet_photo,
#     }
#     return render(request, 'main/photo_edit.html', context)

class DeletePetPhotoView(views.DeleteView):
    model = PetPhoto
    form_class = DeletePetPhotoForm
    template_name = 'main/photo_delete.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


def delete_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeletePetPhotoForm(request.POST, instance=pet_photo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeletePetPhotoForm(instance=pet_photo)

    context = {
        'form': form,
        'pet_photo': pet_photo,
    }

    return render(request, 'main/photo_delete.html', context)


class PetPhotoDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user

        return context


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet-photo-details', pk)
