# Generated by Django 5.1.3 on 2024-12-03 19:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("practitioners", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="practitioner",
            name="user",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="as_practitioner", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="practitioner",
            name="speciality",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="practitioners.speciality"),
        ),
    ]
