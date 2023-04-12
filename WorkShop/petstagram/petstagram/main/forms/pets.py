import datetime

from django import forms

from petstagram.main.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from petstagram.main.models import Pet


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_boostrap_form_controls()
        self.fields['date_of_birth'].required = False

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user = self.user

        if commit:
            pet.save()

        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        BIRTHDAY_YEARS = [i for i in range(1920, int(datetime.datetime.now().year) + 1)]
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter pet name'}
            ),
            'type': forms.Select(
                choices=Pet.ANIMAL_TYPES
            ),
            'date_of_birth': forms.SelectDateWidget(
                years=BIRTHDAY_YEARS
            )
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_boostrap_form_controls()

    class Meta:
        model = Pet
        exclude = ('user_profile',)
        BIRTHDAY_YEARS = [i for i in range(1920, int(datetime.datetime.now().year + 1))]

        widgets = {
            'date_of_birth': forms.SelectDateWidget(
                years=BIRTHDAY_YEARS,
            )
        }


class DeletePetForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    disabled_fields = ('name', 'type', 'date_of_birth')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_boostrap_form_controls()
        self._init_disabled_fields()
        # self.fields['name'].disabled = True
        self.fields['type'].disabled = True
        self.fields['date_of_birth'].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user_profile',)
        BIRTHDAY_YEARS = [i for i in range(1920, int(datetime.datetime.now().year + 1))]
        widgets = {
            'date_of_birth': forms.SelectDateWidget(
                years=BIRTHDAY_YEARS,

            )
        }
