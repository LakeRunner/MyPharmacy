from django.forms import ModelForm, TextInput, NumberInput, Textarea, DateInput
from .models import *
from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100, required=False,
        label='', widget=TextInput(attrs={'placeholder': 'Название',
                                          'class': 'search-input'})
    )
    date_range = forms.CharField(
        max_length=23, required=False,
        label='', widget=forms.TextInput(attrs={'placeholder': 'Дата DD/MM/YYYY - DD/MM/YYYY',
                                                'class': 'search-input'})
    )


class MedicationForm(ModelForm):
    class Meta:
        model = Medications
        fields = ['medication_name', 'medication_description', 'expiration_date']
        widgets = {
            'medication_name': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'medication_description': Textarea(attrs={
                'placeholder': 'Описание'
            }),
            'expiration_date': DateInput(attrs={
                'placeholder': 'Срок годности',
                'format': '%Y-%m-%d'
            })
        }


class DiseaseForm(ModelForm):
    class Meta:
        model = Diseases
        fields = ['disease_name', 'disease_description']
        widgets = {
            'disease_name': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'disease_description': Textarea(attrs={
                'placeholder': 'Описание'
            })
        }


class SymptomForm(ModelForm):
    class Meta:
        model = Symptoms
        fields = ['symptom_name']
        widgets = {
            'symptom_name': TextInput(attrs={
                'placeholder': 'Название'
            })
        }
