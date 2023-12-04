from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import *


class MedicationDetailView(DetailView):
    model = Medications
    template_name = 'main/medication.html'
    context_object_name = 'medication'
    title = 'Информация о лекарстве'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class MedicationUpdateView(UpdateView):
    model = Medications
    template_name = 'main/edit_medication.html'
    title = 'Изменить лекарство'
    form_class = MedicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class MedicationDeleteView(DeleteView):
    model = Medications
    template_name = 'main/delete_medication.html'
    title = 'Удалить лекарство'
    context_object_name = 'medication'
    success_url = '/medications/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def delete(self, request, *args, **kwargs):
        medication = self.get_object()
        MedicationDiseaseLink.objects.filter(medication=medication).delete()
        return super().delete(request, *args, **kwargs)


class DiseaseDetailView(DetailView):
    model = Diseases
    template_name = 'main/disease.html'
    context_object_name = 'disease'
    title = 'Информация о лекарстве'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        disease_id = self.kwargs.get('pk')
        medication_links = MedicationDiseaseLink.objects.filter(disease__disease_id=disease_id)
        med = set(link.medication.medication_name for link in medication_links)
        symptom_links = DiseaseSymptomLink.objects.filter(disease__disease_id=disease_id)
        sym = [link.symptom.symptom_name for link in symptom_links]
        context['title'] = 'Информация о болезни'
        context['medications'] = med
        context['symptoms'] = sym
        return context


class DiseaseUpdateView(UpdateView):
    model = Diseases
    template_name = 'main/edit_disease.html'
    title = 'Изменить болезнь'
    form_class = DiseaseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class DiseaseDeleteView(DeleteView):
    model = Diseases
    template_name = 'main/delete_disease.html'
    title = 'Удалить болезнь'
    context_object_name = 'disease'
    success_url = '/diseases/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def delete(self, request, *args, **kwargs):
        disease = self.get_object()
        DiseaseSymptomLink.objects.filter(disease=disease).delete()
        MedicationDiseaseLink.objects.filter(disease=disease).delete()
        return super().delete(request, *args, **kwargs)


class SymptomUpdateView(UpdateView):
    model = Symptoms
    template_name = 'main/edit_symptom.html'
    title = 'Изменить симптом'
    form_class = SymptomForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class SymptomDeleteView(DeleteView):
    model = Symptoms
    template_name = 'main/delete_symptom.html'
    title = 'Удалить симптом'
    context_object_name = 'symptom'
    success_url = '/symptoms/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def delete(self, request, *args, **kwargs):
        symptom = self.get_object()
        DiseaseSymptomLink.objects.filter(symptom=symptom).delete()
        return super().delete(request, *args, **kwargs)


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


def add_medication(request):
    error = ''
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medications')
        else:
            error = 'Форма была заполнена неверно!'
    else:
        form = MedicationForm()
    data = {
        'error': error,
        'title': 'Добавить лекарство',
        'form': form
    }
    return render(request, 'main/add_medication.html', data)


def diseases(request):
    dis = list(enumerate(Diseases.objects.all(), start=1))
    data = {
        'title': 'Болезни',
        'diseases': dis,
    }
    return render(request, 'main/diseases.html', data)


def add_disease(request):
    error = ''
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diseases')
        else:
            error = 'форма была заполнена неверно'
    else:
        form = DiseaseForm()
    data = {
        'error': error,
        'title': 'Добавить болезнь',
        'form': form
    }
    return render(request, 'main/add_disease.html', data)


def symptoms(request):
    sym = list(enumerate(Symptoms.objects.all(), start=1))
    data = {
        'title': 'Симптомы',
        'symptoms': sym,
    }
    return render(request, 'main/symptoms.html', data)


def add_symptom(request):
    error = ''
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('symptoms')
        else:
            error = 'Форма была заполнена неверна'
    else:
        form = SymptomForm()
    data = {
        'error': error,
        'title': 'Добавить симптом',
        'form': form
    }
    return render(request, 'main/add_symptom.html', data)
