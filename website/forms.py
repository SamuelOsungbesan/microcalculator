from django import forms
from .models import Specimen

class SpecimenForm(forms.ModelForm):
    class Meta:
        model = Specimen
        fields = ['name', 'size', 'mag_factor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'mag_factor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }