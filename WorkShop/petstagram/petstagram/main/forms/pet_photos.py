from django import forms

from petstagram.common.helpers import BootstrapFormMixin
from petstagram.main.models import PetPhoto


class CreatePetPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_boostrap_form_controls()
        self.fields['description'].required = False
        # self.fields['photo'].required = True

    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        labels = {
            'photo': 'Pet Image',
            'tagged_pets': 'Tag Pets',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description',
                       'rows': 3},
            ),
            'tagged_pets': forms.SelectMultiple(
            )
        }


class EditPetPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_boostrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets',)
        labels = {
            'tagged_pets': 'Tag Pets'
        }
        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 3}
            )
        }


class DeletePetPhotoForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = PetPhoto
        fields = ()