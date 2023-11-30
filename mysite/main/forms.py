from django import forms
from .models import *


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medications
        fields = ['medication_name', 'medication_description', 'expiration_date']


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Diseases
        fields = ['disease_name', 'disease_description']


class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptoms
        fields = ['symptom_name']