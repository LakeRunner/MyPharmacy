from django.shortcuts import render


def index(request):
    data = {
        'title': 'Домашняя аптечка'
    }
    return render(request, 'main/index.html', data)


def medications(request):
    data = {
        'title': 'Лекарства'
    }
    return render(request, 'main/medications.html', data)


def diseases(request):
    data = {
        'title': 'Болезни'
    }
    return render(request, 'main/diseases.html', data)


def symptoms(request):
    data = {
        'title': 'Симптомы'
    }
    return render(request, 'main/symptoms.html', data)
