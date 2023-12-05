from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import *


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
