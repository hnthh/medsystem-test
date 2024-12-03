import pytest

from apps.encounters.models import Encounter

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.freeze_time("2032-01-07"),
]

url = "/api/v1/ehr/encounters/"


@pytest.fixture(autouse=True)
def encounter(factory):
    return factory.encounter(status=Encounter.Status.STARTED)


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        (Encounter.Status.STARTED, 1),
        (Encounter.Status.CONFIRMED, 0),
    ],
)
def test_response_filtered_status(as_practitioner, expected, query):
    response = as_practitioner.get(f"{url}?status={query}")

    assert len(response) == expected
