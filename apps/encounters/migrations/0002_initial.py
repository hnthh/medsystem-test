# Generated by Django 5.1.3 on 2024-12-03 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("encounters", "0001_initial"),
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="encounter",
            name="patient",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="patients.patient"),
        ),
    ]