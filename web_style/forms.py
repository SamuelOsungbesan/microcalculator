from django import forms
from .models import Specimen

class SpecimenForm(forms.ModelForm):
    class Meta:
        model = Specimen
        fields = ['name', 'magnified_size', 'magnification_factor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'magnified_size': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'magnification_factor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }