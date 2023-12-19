from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('medications/', views.medications, name='medications'),
    path('medications/<int:pk>/', views.MedicationDetailView.as_view(), name='medication'),
    path('medications/<int:pk>/edit/', views.MedicationUpdateView.as_view(), name='edit_medication'),
    path('medications/<int:pk>/delete/', views.MedicationDeleteView.as_view(), name='delete_medication'),
    path('medications/add/', views.add_medication, name='add_medication'),
    path('diseases/', views.diseases, name='diseases'),
    path('diseases/<int:pk>/', views.DiseaseDetailView.as_view(), name='disease'),
    path('diseases/<int:pk>/edit/', views.DiseaseUpdateView.as_view(), name='edit_disease'),
    path('diseases/<int:pk>/delete/', views.DiseaseDeleteView.as_view(), name='delete_disease'),
    path('diseases/add/', views.add_disease, name='add_disease'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('symptoms/<int:pk>/', views.SymptomDetailView.as_view(), name='symptom'),
    path('symptoms/<int:pk>/edit/', views.SymptomUpdateView.as_view(), name='edit_symptom'),
    path('symptoms/<int:pk>/delete/', views.SymptomDeleteView.as_view(), name='delete_symptom'),
    path('symptoms/add/', views.add_symptom, name='add_symptom'),
]
