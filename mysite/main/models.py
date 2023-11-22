from django.db import models


class Diseases(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=255, blank=True, null=True)
    disease_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Болезнь'
        verbose_name_plural = 'Болезни'
        managed = False
        db_table = 'diseases'


class Symptoms(models.Model):
    symptom_id = models.AutoField(primary_key=True)
    symptom_name = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Симптом'
        verbose_name_plural = 'Симптомы'
        managed = False
        db_table = 'symptoms'


class DiseaseSymptomLink(models.Model):
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE, primary_key=True)
    symptom = models.ForeignKey(Symptoms, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Связь болезни и симптома'
        verbose_name_plural = 'Связи болезней и симптомов'
        managed = False
        db_table = 'disease_symptom_link'
        unique_together = (('disease', 'symptom'),)


class Medications(models.Model):
    medication_id = models.AutoField(primary_key=True)
    medication_name = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    medication_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Лекарство'
        verbose_name_plural = 'Лекарства'
        managed = False
        db_table = 'medications'


class MedicationDiseaseLink(models.Model):
    medication = models.ForeignKey(Medications, on_delete=models.CASCADE, primary_key=True)
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Связь лекарства и болезни'
        verbose_name_plural = 'Связь лекарства и болезней'
        managed = False
        db_table = 'medication_disease_link'
        unique_together = (('medication', 'disease'),)
