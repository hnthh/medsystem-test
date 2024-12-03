from rest_framework import serializers

from apps.locations.models import Location


class LocationReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "legal_address",
            "name",
            "physical_address",
            "type",
        )
        model = Location
        read_only_fields = fields
