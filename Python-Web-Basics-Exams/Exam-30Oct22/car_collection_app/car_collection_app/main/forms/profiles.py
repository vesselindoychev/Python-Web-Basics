from django import forms

from car_collection_app.main.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput()
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

        widgets = {
            'password': forms.PasswordInput()
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        cars = Car.objects.all()
        cars.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
