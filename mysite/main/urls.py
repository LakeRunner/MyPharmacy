from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('medications/', views.medications, name='medications'),
    path('diseases/', views.diseases, name='diseases'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('medication/<int:medication_id>/', views.medication, name='medication'),
    path('disease/<int:disease_id>/', views.disease, name='disease'),
]
