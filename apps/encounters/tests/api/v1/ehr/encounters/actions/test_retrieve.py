import pytest
from pytest_lazy_fixtures import lf
from rest_framework import status

pytestmark = pytest.mark.django_db


@pytest.fixture()
def url(encounter):
    return f"/api/v1/ehr/encounters/{encounter.id}/"


def test_response(as_practitioner, assert_dt, encounter, faker, url, utc):  # noqa: PLR0913
    encounter.update(ended_at=faker.past_datetime(tzinfo=utc))

    response = as_practitioner.get(url)

    assert response["id"] == encounter.id
    assert response["practitioner"] == encounter.practitioner_id
    assert response["status"] == encounter.status
    assert_dt(response["createdAt"], encounter.created_at)
    assert_dt(response["endedAt"], encounter.ended_at)
    assert_dt(response["startedAt"], encounter.started_at)

    assert set(response) == {
        "id",
        "createdAt",
        "endedAt",
        "location",
        "patient",
        "practitioner",
        "startedAt",
        "status",
    }


def test_location_response(as_practitioner, encounter, url):
    response = as_practitioner.get(url)["location"]

    location = encounter.location
    assert response["id"] == location.id
    assert response["legalAddress"] == location.legal_address
    assert response["name"] == location.name
    assert response["physicalAddress"] == location.physical_address
    assert response["type"] == location.type

    assert set(response) == {
        "id",
        "legalAddress",
        "name",
        "physicalAddress",
        "type",
    }


def test_patient_response(as_practitioner, encounter, url):
    response = as_practitioner.get(url)["patient"]

    patient = encounter.patient
    assert response["id"] == patient.id
    assert response["fname"] == patient.fname
    assert response["lname"] == patient.lname
    assert response["mname"] == patient.mname
    assert response["email"] == patient.email
    assert response["phone"] == patient.phone

    assert set(response) == {
        "id",
        "fname",
        "lname",
        "mname",
        "email",
        "phone",
    }


@pytest.mark.parametrize(
    ("requester", "expected_status"),
    [
        (lf("as_anon"), status.HTTP_401_UNAUTHORIZED),
        (lf("as_patient"), status.HTTP_403_FORBIDDEN),
        (lf("as_admin"), status.HTTP_200_OK),
    ],
)
def test_permissions(expected_status, requester, url):
    requester.get(url, expected_status_code=expected_status)
