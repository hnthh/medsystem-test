import pytest
from pytest_lazy_fixtures import lf
from rest_framework import status

from apps.encounters.models import Encounter

pytestmark = pytest.mark.django_db


@pytest.fixture()
def encounter(encounter):
    return encounter.update(status=Encounter.Status.STARTED)


@pytest.fixture()
def url(encounter):
    return f"/api/v1/ehr/encounters/{encounter.id}/"


def test_encounter_deleted(as_practitioner, url):
    as_practitioner.delete(url)

    assert not Encounter.objects.exists()


@pytest.mark.parametrize(
    ("requester", "expected_status"),
    [
        (lf("as_anon"), status.HTTP_401_UNAUTHORIZED),
        (lf("as_admin"), status.HTTP_204_NO_CONTENT),
        (lf("as_patient"), status.HTTP_403_FORBIDDEN),
    ],
)
def test_permissions(expected_status, requester, url):
    requester.delete(url, expected_status_code=expected_status)
