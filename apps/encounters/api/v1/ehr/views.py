from apps.encounters.api.v1.ehr.serializers import EncounterCreateSerializer, EncounterReadSerializer, EncounterUpdateSerializer
from apps.encounters.models import Encounter
from core.api.permissions import AllowAdmin, AllowPractitioner
from core.api.views import BaseModelViewSet


class EncounterView(BaseModelViewSet):
    permission_classes = (AllowAdmin | AllowPractitioner,)
    queryset = Encounter.objects.for_view()
    serializer_action_classes = {
        "create": EncounterCreateSerializer,
        "partial_update": EncounterUpdateSerializer,
    }
    serializer_class = EncounterReadSerializer
