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
    med = get_object_or_404(Medications, pk=pk)
    data = {'title': 'Изменить лекарство',
            'medication': med}
    if request.method == 'POST':
        med.medication_name = request.POST['medication_name']
        med.expiration_date = request.POST['expiration_date']
        med.medication_description = request.POST['medication_description']
        med.save()
        return redirect('medications')
    return render(request, 'main/edit_medication.html', data)


def delete_medication(request, pk):
    med = get_object_or_404(Medications, pk=pk)
    data = {'medication': med,
            'title': 'Удаление лекарства'}
    if request.method == 'POST':
        MedicationDiseaseLink.objects.filter(medication=med).delete()
        med.delete()
        return redirect('medications')
    return render(request, 'main/delete_medication.html', data)


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
    dis = get_object_or_404(Diseases, pk=pk)
    data = {'title': 'Изменить болезнь',
            'disease': dis}
    if request.method == 'POST':
        dis.disease_name = request.POST['disease_name']
        dis.disease_description = request.POST['disease_description']
        dis.save()
        return redirect('diseases')
    return render(request, 'main/edit_disease.html', data)


def delete_disease(request, pk):
    dis = get_object_or_404(Diseases, pk=pk)
    data = {'disease': dis,
            'title': 'Удаление болезни'}
    if request.method == 'POST':
        MedicationDiseaseLink.objects.filter(disease=dis).delete()
        DiseaseSymptomLink.objects.filter(disease=dis).delete()
        dis.delete()
        return redirect('diseases')
    return render(request, 'main/delete_disease.html', data)


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
    sym = get_object_or_404(Symptoms, pk=pk)
    data = {'title': 'Изменить симптом',
            'symptom': sym}
    if request.method == 'POST':
        sym.symptom_name = request.POST['symptom_name']
        sym.save()
        return redirect('symptoms')
    return render(request, 'main/edit_symptom.html', data)


def delete_symptom(request, pk):
    sym = get_object_or_404(Symptoms, pk=pk)
    data = {'symptom': sym,
            'title': 'Удаление симптома'}
    if request.method == 'POST':
        DiseaseSymptomLink.objects.filter(symptom=sym).delete()
        sym.delete()
        return redirect('symptoms')
    return render(request, 'main/delete_symptom.html', data)


def add_symptom(request):
    pass
