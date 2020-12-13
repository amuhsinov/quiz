from django import forms
from cars.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        widgets = {
            'name': forms.TextInput(),
            'image': forms.FileInput(),
        }
        exclude = ('fk_user_id',)
