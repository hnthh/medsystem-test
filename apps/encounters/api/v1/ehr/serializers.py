from rest_framework import serializers

from apps.encounters.models import Encounter
from apps.locations.api.v1.ehr.serializers import LocationReadSerializer
from apps.patients.api.v1.ehr.serializers import PatientReadSerializer
from apps.practitioners.api.v1.ehr.serializers import CurrentPractitionerDefault


class EncounterCreateSerializer(serializers.ModelSerializer):
    practitioner = serializers.HiddenField(default=CurrentPractitionerDefault())

    class Meta:
        fields = (
            "location",
            "patient",
            "practitioner",
            "started_at",
        )
        model = Encounter


class EncounterReadSerializer(serializers.ModelSerializer):
    location = LocationReadSerializer()
    patient = PatientReadSerializer()

    class Meta:
        fields = (
            "id",
            "ended_at",
            "location",
            "patient",
            "practitioner",
            "started_at",
            "status",
        )
        model = Encounter
        read_only_fields = fields


class EncounterUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("status",)
        model = Encounter
