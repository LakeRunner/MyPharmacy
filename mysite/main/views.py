from django.shortcuts import render, get_object_or_404, redirect
from .models import Medications, Diseases, Symptoms, MedicationDiseaseLink, DiseaseSymptomLink


def index(request):
    data = {
        'title': 'Домашняя аптечка'
    }
    return render(request, 'main/index.html', data)


def medications(request):
    med = list(enumerate(Medications.objects.all(), start=1))
    data = {
        'title': 'Лекарства',
        'medications': med,
    }
    return render(request, 'main/medications.html', data)


def medication(request, medication_id):
    med = get_object_or_404(Medications, medication_id=medication_id)
    data = {
        'title': 'Информация о лекарстве',
        'name': med.medication_name,
        'description': med.medication_description,
    }
    return render(request, 'main/medication.html', data)


def edit_medication(request, pk):
    pass


def delete_medication(request, pk):
    med = get_object_or_404(Medications, pk=pk)
    MedicationDiseaseLink.objects.filter(medication=med).delete()
    med.delete()
    return redirect('medications')


def add_medication(request):
    pass


def diseases(request):
    dis = list(enumerate(Diseases.objects.all(), start=1))
    data = {
        'title': 'Болезни',
        'diseases': dis,
    }
    return render(request, 'main/diseases.html', data)


def disease(request, disease_id):
    dis = get_object_or_404(Diseases, disease_id=disease_id)
    med = set()
    sym = set()
    medication_links = MedicationDiseaseLink.objects.all()
    symptom_links = DiseaseSymptomLink.objects.all()
    for i in medication_links:
        if i.disease.disease_id == disease_id:
            med.add(get_object_or_404(Medications, medication_id=i.medication.medication_id).medication_name)
    for i in symptom_links:
        if i.disease.disease_id == disease_id:
            sym.add(get_object_or_404(Symptoms, symptom_id=i.symptom.symptom_id).symptom_name)

    data = {
        'title': 'Информация о болезни',
        'name': dis.disease_name,
        'description': dis.disease_description,
        'symptoms': sym,
        'medications': med,
    }
    return render(request, 'main/disease.html', data)


def edit_disease(request, pk):
    pass


def delete_disease(request, pk):
    pass


def add_disease(request):
    pass


def symptoms(request):
    sym = list(enumerate(Symptoms.objects.all(), start=1))
    data = {
        'title': 'Симптомы',
        'symptoms': sym,
    }
    return render(request, 'main/symptoms.html', data)


def edit_symptom(request, pk):
    pass


def delete_symptom(request, pk):
    pass


def add_symptom(request):
    pass
