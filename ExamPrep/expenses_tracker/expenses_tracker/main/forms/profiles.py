from django import forms

from expenses_tracker.main.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image'
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image'
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        Expense.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
