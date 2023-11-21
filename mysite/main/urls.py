from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('medications/', views.medications, name='medications'),
    path('diseases/', views.diseases, name='diseases'),
    path('symptoms/', views.symptoms, name='symptoms')
]
