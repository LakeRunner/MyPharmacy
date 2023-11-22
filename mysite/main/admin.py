from django.contrib import admin
from .models import *


admin.site.register(Diseases)
admin.site.register(Medications)
admin.site.register(Symptoms)
admin.site.register(MedicationDiseaseLink)
admin.site.register(DiseaseSymptomLink)
