from django.shortcuts import render, get_object_or_404
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


def diseases(request):
    dis = list(enumerate(Diseases.objects.all(), start=1))
    data = {
        'title': 'Болезни',
        'diseases': dis,
    }
    return render(request, 'main/diseases.html', data)


def disease(request, disease_id):
    dis = get_object_or_404(Diseases, disease_id=disease_id)
    sym = []
    med = []
    medication_links = MedicationDiseaseLink.objects.all()
    symptom_links = DiseaseSymptomLink.objects.all()
    print(medication_links)
    print(symptom_links)
    #for i in medication_links:
    #    if i.disease == disease_id:
    #        med.append(get_object_or_404(Medications, medication_id=i.medication))
    #for i in symptom_links:
    #    if i.disease == disease_id:
    #        sym.append(get_object_or_404(Symptoms, sumptom_id=i.symptom))

    #med = [link.medication for link in medication_links]
    #sym = [link.symptom for link in symptom_links]

    data = {
        'title': 'Информация о болезни',
        'name': dis.disease_name,
        'description': dis.disease_description,
        'symptoms': sym,
        'medications': med,
    }
    return render(request, 'main/disease.html', data)


def symptoms(request):
    sym = list(enumerate(Symptoms.objects.all(), start=1))
    data = {
        'title': 'Симптомы',
        'symptoms': sym,
    }
    return render(request, 'main/symptoms.html', data)
