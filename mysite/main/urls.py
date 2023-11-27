from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('medications/', views.medications, name='medications'),
    path('medication/<int:medication_id>/', views.medication, name='medication'),
    path('medications/<int:pk>/edit/', views.edit_medication, name='edit_medication'),
    path('medications/<int:pk>/delete/', views.delete_medication, name='delete_medication'),
    path('medications/add/', views.add_medication, name='add_medication'),
    path('diseases/', views.diseases, name='diseases'),
    path('disease/<int:disease_id>/', views.disease, name='disease'),
    path('diseases/<int:pk>/edit/', views.edit_disease, name='edit_disease'),
    path('diseases/<int:pk>/delete/', views.delete_disease, name='delete_disease'),
    path('diseases/add/', views.add_disease, name='add_disease'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('symptoms/<int:pk>/edit/', views.edit_symptom, name='edit_symptom'),
    path('symptoms/<int:pk>/delete/', views.delete_symptom, name='delete_symptom'),
    path('symptoms/add/', views.add_symptom, name='add_symptom'),
]
