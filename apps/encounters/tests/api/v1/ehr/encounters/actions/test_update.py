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


@pytest.fixture()
def data():
    return {
        "status": Encounter.Status.COMPLETED,
    }


def test_encounter_status_updated(as_practitioner, data, encounter, url):
    as_practitioner.patch(url, data=data)

    assert encounter.refresh().status == data["status"]


@pytest.mark.parametrize(
    ("requester", "expected_status"),
    [
        (lf("as_anon"), status.HTTP_401_UNAUTHORIZED),
        (lf("as_admin"), status.HTTP_200_OK),
        (lf("as_patient"), status.HTTP_403_FORBIDDEN),
    ],
)
def test_permissions(data, expected_status, requester, url):
    requester.patch(url, data=data, expected_status_code=expected_status)
