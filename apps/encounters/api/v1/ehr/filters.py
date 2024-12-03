from django.db.models import Q
from django_filters import rest_framework as filters

from apps.encounters.models import Encounter


class EncounterFilters(filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter()
    patient = filters.CharFilter(method="_filter_by_full_name")
    practitioner = filters.CharFilter(method="_filter_by_full_name")

    class Meta:
        fields = (
            "created_at",
            "patient",
            "practitioner",
            "status",
        )
        model = Encounter

    def _filter_by_full_name(self, queryset, name, value):
        cleaned_value = value.strip()

        match_by_full_name = Q()
        for value_part in cleaned_value.split():
            match_by_full_name |= (
                Q(**{f"{name}__fname__icontains": value_part}) | Q(**{f"{name}__lname__icontains": value_part}) | Q(**{f"{name}__mname__icontains": value_part})
            )

        return queryset.filter(match_by_full_name).distinct()
