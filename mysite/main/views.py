from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import *


class MedicationDetailView(DetailView):
    model = Medications
    template_name = 'main/medication.html'
    context_object_name = 'medication'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medication_id = self.kwargs.get('pk')
        disease_links = MedicationDiseaseLink.objects.filter(medication__medication_id=medication_id)
        dis = set(link.disease.disease_name for link in disease_links)
        context['diseases'] = dis
        return context


class MedicationUpdateView(UpdateView):
    model = Medications
    template_name = 'main/edit_medication.html'
    form_class = MedicationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        disease_id = self.kwargs.get('pk')
        medication_links = MedicationDiseaseLink.objects.filter(disease__disease_id=disease_id)
        med = set(link.medication.medication_name for link in medication_links)
        symptom_links = DiseaseSymptomLink.objects.filter(disease__disease_id=disease_id)
        sym = [link.symptom.symptom_name for link in symptom_links]
        context['medications'] = med
        context['symptoms'] = sym
        return context


class DiseaseUpdateView(UpdateView):
    model = Diseases
    template_name = 'main/edit_disease.html'
    form_class = DiseaseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DiseaseDeleteView(DeleteView):
    model = Diseases
    template_name = 'main/delete_disease.html'
    context_object_name = 'disease'
    success_url = '/diseases/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def delete(self, request, *args, **kwargs):
        disease = self.get_object()
        DiseaseSymptomLink.objects.filter(disease=disease).delete()
        MedicationDiseaseLink.objects.filter(disease=disease).delete()
        return super().delete(request, *args, **kwargs)


class SymptomDetailView(DetailView):
    model = Symptoms
    template_name = 'main/symptom.html'
    context_object_name = 'symptom'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        symptom_id = self.kwargs.get('pk')
        disease_links = DiseaseSymptomLink.objects.filter(symptom__symptom_id=symptom_id)
        dis = set(link.disease.disease_name for link in disease_links)
        context['diseases'] = dis
        return context


class SymptomUpdateView(UpdateView):
    model = Symptoms
    template_name = 'main/edit_symptom.html'
    form_class = SymptomForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SymptomDeleteView(DeleteView):
    model = Symptoms
    template_name = 'main/delete_symptom.html'
    context_object_name = 'symptom'
    success_url = '/symptoms/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def delete(self, request, *args, **kwargs):
        symptom = self.get_object()
        DiseaseSymptomLink.objects.filter(symptom=symptom).delete()
        return super().delete(request, *args, **kwargs)


def index(request):
    return render(request, 'main/index.html')


def medications(request):
    med = list(enumerate(Medications.objects.all(), start=1))
    form = SearchForm(request.GET)
    data = {
        'medications': med,
        'form': form
    }
    if form.is_valid() and form.cleaned_data['search']:
        search = form.cleaned_data['search']
        searched = list(enumerate(Medications.objects.filter(medication_name__istartswith=search)))
        data['medications'] = searched
        data['search'] = search
        return render(request, 'main/searched_medications.html', data)
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
    form = SearchForm(request.GET)
    data = {
        'diseases': dis,
        'form': form
    }
    if form.is_valid() and form.cleaned_data['search']:
        search = form.cleaned_data['search']
        searched = list(enumerate(Diseases.objects.filter(disease_name__istartswith=search)))
        data['diseases'] = searched
        data['search'] = search
        return render(request, 'main/searched_diseases.html', data)
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
    form = SearchForm(request.GET)
    data = {
        'symptoms': sym,
        'form': form
    }
    if form.is_valid() and form.cleaned_data['search']:
        search = form.cleaned_data['search']
        searched = list(enumerate(Symptoms.objects.filter(symptom_name__istartswith=search)))
        data['symptoms'] = searched
        data['search'] = search
        return render(request, 'main/searched_symptoms.html', data)
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
