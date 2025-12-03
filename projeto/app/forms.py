from django import forms
from .models import InfoCad

class InfoCadForm(forms.ModelForm):
    class Meta:
        model = InfoCad
        fields = ['nome', 'idade'] 
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ex: Maria Silva'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': '25'}),
        }
        labels = {
            'nome': 'Nome completo:',
            'idade': 'Idade:',
        }