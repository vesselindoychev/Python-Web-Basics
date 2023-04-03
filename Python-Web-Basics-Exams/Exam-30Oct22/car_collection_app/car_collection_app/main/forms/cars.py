from django import forms

from car_collection_app.main.custom_validators import DisabledFieldsFormMixin
from car_collection_app.main.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'image_url': 'Image URL'
        }


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'image_url': 'Image URL'
        }


class DeleteCarForm(DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled_fields()
        self.fields['type'].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
        }
