from django import forms

from my_plant_app.main.models import Profile, Plant


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('picture',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'picture': 'Profile Picture'
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        plants = Plant.objects.all()
        plants.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
