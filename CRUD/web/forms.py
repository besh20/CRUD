from django import forms
from .models import *

class studForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['sid', 'first_name', 'last_name', 'batch', 'email', 'grade']
        labels = {
            'sid': 'Sid',
            'first_name': 'First Name', 
            'last_name': 'Last Name', 
            'batch': 'Batch', 
            'email': 'Email', 
            'grade': 'Grade'
        }
        widgets = {
            'sid': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'batch': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control'}),
        }