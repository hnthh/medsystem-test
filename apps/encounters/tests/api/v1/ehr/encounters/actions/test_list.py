import pytest
from pytest_lazy_fixtures import lf
from rest_framework import status

pytestmark = pytest.mark.django_db


url = "/api/v1/ehr/encounters/"


@pytest.fixture()
def retrieve(as_practitioner, encounter):
    return lambda: as_practitioner.get(f"/api/v1/ehr/encounters/{encounter.id}/")


def test_response(as_practitioner, retrieve):
    response = as_practitioner.get(url)[0]

    assert response == retrieve()


@pytest.mark.parametrize("count", [1, 2])
def test_perfomance(as_practitioner, count, django_assert_num_queries, factory):
    factory.cycle(count).encounter()

    with django_assert_num_queries(4):
        as_practitioner.get(url)


@pytest.mark.parametrize(
    ("requester", "expected_status"),
    [
        (lf("as_anon"), status.HTTP_401_UNAUTHORIZED),
        (lf("as_patient"), status.HTTP_403_FORBIDDEN),
        (lf("as_admin"), status.HTTP_200_OK),
    ],
)
def test_permissions(expected_status, requester):
    requester.get(url, expected_status_code=expected_status)
