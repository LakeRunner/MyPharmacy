from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('disease_id', models.AutoField(primary_key=True, serialize=False)),
                ('disease_name', models.CharField(blank=True, max_length=255, null=True)),
                ('disease_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'diseases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DiseaseSymptomLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'disease_symptom_link',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedicationDiseaseLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'medication_disease_link',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medications',
            fields=[
                ('medication_id', models.AutoField(primary_key=True, serialize=False)),
                ('medication_name', models.CharField(blank=True, max_length=255, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('medication_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'medications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('symptom_id', models.AutoField(primary_key=True, serialize=False)),
                ('symptom_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'symptoms',
                'managed': False,
            },
        ),
    ]
