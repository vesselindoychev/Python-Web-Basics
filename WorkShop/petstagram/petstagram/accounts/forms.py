import datetime

from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from petstagram.accounts.models import Profile
from petstagram.common.helpers import BootstrapFormMixin
from petstagram.main.models import PetPhoto


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    YEARS = []
    today = datetime.date.today()
    year = today.year
    for i in range(1920, year + 1):
        YEARS.append(i)
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter first name'}
        )
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter last name'}
        )
    )

    picture = forms.URLField(
        widget=forms.URLInput(
            attrs={'placeholder': 'Enter URL'}
        ),
        label='Link to Profile Picture'
    )
    #
    # date_of_birth = forms.DateField(
    #     widget=forms.SelectDateWidget(
    #         years=YEARS
    #     )
    # )
    # description = forms.CharField(
    #     widget=forms.Textarea()
    # )
    # email = forms.EmailField()
    # gender = forms.ChoiceField(
    #     choices=((g, g) for g in Profile.GENDERS),
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_boostrap_form_controls()
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Enter password', 'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Enter password again', 'class': 'form-control'}, )
        self.fields['password2'].label = 'Confirm Password'

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            # date_of_birth=self.cleaned_data['date_of_birth'],
            # description=self.cleaned_data['description'],
            # email=self.cleaned_data['email'],
            # gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture')

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter username'
                }
            ),
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_boostrap_form_controls()
        # self.initial['gender'] = Profile.DO_NOT_SHOW
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
        # should be done with signals
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'description', 'date_of_birth', 'email', 'gender', 'picture')
