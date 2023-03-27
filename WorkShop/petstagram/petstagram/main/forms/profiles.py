import datetime

from django import forms

from petstagram.main.helpers import BootstrapFormMixin
from petstagram.main.models import Profile, PetPhoto


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_boostrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter first name'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter last name'}
            ),
            'picture': forms.URLInput(
                attrs={'placeholder': 'Enter URL'}
            )
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_boostrap_form_controls()
        self.initial['gender'] = 'Do not show'
        # self.fields['gender'].initial = 'Do not show'

    class Meta:
        model = Profile
        fields = '__all__'

        present_year = int((datetime.datetime.now()).year)
        BIRTHDAY_YEARS = [i for i in range(1920, present_year + 1)]

        widgets = {
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter email'}
            ),
            'gender': forms.Select(
                choices=Profile.GENDERS,

            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description',
                       'rows': 3
                       }
            ),
            'date_of_birth': forms.SelectDateWidget(
                years=BIRTHDAY_YEARS
            )

        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pets = self.instance.pet_set.all()
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'description', 'date_of_birth', 'email', 'gender', 'picture')

