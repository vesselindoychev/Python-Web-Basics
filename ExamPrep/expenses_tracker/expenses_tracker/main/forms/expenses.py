from django import forms

from expenses_tracker.main.models import Expense


class CreateExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'image': 'Link to Image'
        }


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'image': 'Link to Image'
        }


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        # self.fields['title'].novalidate = True
        self.fields['description'].disabled = True
        self.fields['image'].disabled = True
        self.fields['price'].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'image': 'Link to Image'
        }