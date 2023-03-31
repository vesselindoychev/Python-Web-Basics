from django import forms

from my_plant_app.main.models import Plant


class CreatePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'image': 'Image URL'
        }


class EditPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'image': 'Image URL',
        }


class DeletePlantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].disabled = True
        self.fields['name'].disabled = True
        self.fields['image'].disabled = True
        self.fields['description'].disabled = True
        self.fields['price'].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'image': 'Image URL',
        }
