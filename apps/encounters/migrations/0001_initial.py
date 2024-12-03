# Generated by Django 5.1.3 on 2024-12-03 19:54

import django.db.models.deletion
from django.db import migrations, models

import core.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("locations", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Encounter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("completed", "Completed"), ("confirmed", "Confirmed"), ("paid", "Paid"), ("pending", "Pending"), ("started", "Started")],
                        default="started",
                        max_length=32,
                    ),
                ),
                ("ended_at", models.DateTimeField(blank=True, null=True)),
                ("started_at", models.DateTimeField()),
                ("location", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="locations.location")),
            ],
            options={
                "abstract": False,
                "default_related_name": "encounters",
            },
            bases=(models.Model, core.models.AppModelMixin),
        ),
    ]