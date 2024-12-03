from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from apps.encounters.api.v1.ehr.filters import EncounterFilters
from apps.encounters.api.v1.ehr.serializers import EncounterCreateSerializer, EncounterReadSerializer, EncounterUpdateSerializer
from apps.encounters.models import Encounter
from core.api.permissions import AllowAdmin, AllowPractitioner
from core.api.views import BaseModelViewSet


class EncounterView(BaseModelViewSet):
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = EncounterFilters
    ordering_fields = ("created_at",)
    permission_classes = (AllowAdmin | AllowPractitioner,)
    queryset = Encounter.objects.for_view()
    serializer_action_classes = {
        "create": EncounterCreateSerializer,
        "partial_update": EncounterUpdateSerializer,
    }
    serializer_class = EncounterReadSerializer
