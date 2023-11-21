from django.db import models


class DiseaseSymptomLink(models.Model):
    disease_id = models.ForeignKey('Diseases', models.DO_NOTHING, blank=True, null=True)
    symptom_id = models.ForeignKey('Symptoms', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease_symptom_link'


class Diseases(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=255, blank=True, null=True)
    disease_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diseases'


class MedicationDiseaseLink(models.Model):
    medication_id = models.ForeignKey('Medications', models.DO_NOTHING, blank=True, null=True)
    disease_id = models.ForeignKey(Diseases, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medication_disease_link'


class Medications(models.Model):
    medication_id = models.AutoField(primary_key=True)
    medication_name = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    medication_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medications'


class Symptoms(models.Model):
    symptom_id = models.AutoField(primary_key=True)
    symptom_name = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'symptoms'
