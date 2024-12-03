import pytest
from pytest_lazy_fixtures import lf
from rest_framework import status

from apps.encounters.models import Encounter

pytestmark = pytest.mark.django_db


url = "/api/v1/ehr/encounters/"


@pytest.fixture()
def data(faker, location, patient, utc):
    return {
        "location": location.id,
        "patient": patient.id,
        "started_at": faker.past_datetime(tzinfo=utc),
    }


def test_encounter_created(as_practitioner, data):
    as_practitioner.post(url, data=data)

    encounter = Encounter.objects.get()
    assert encounter.location_id == data["location"]
    assert encounter.patient_id == data["patient"]
    assert encounter.started_at == data["started_at"]


@pytest.mark.parametrize(
    ("requester", "expected_status"),
    [
        (lf("as_anon"), status.HTTP_401_UNAUTHORIZED),
        (lf("as_patient"), status.HTTP_403_FORBIDDEN),
    ],
)
def test_permissions(data, expected_status, requester):
    requester.post(url, data=data, expected_status_code=expected_status)
