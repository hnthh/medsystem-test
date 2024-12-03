from rest_framework import serializers

from apps.patients.models import Patient


class PatientReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "fname",
            "lname",
            "mname",
            "email",
            "phone",
        )
        model = Patient
        read_only_fields = fields
