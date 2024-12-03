import pytest

pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True)
def _encounters(factory, faker, utc):
    for encounter in factory.cycle(3).encounter():
        encounter.update(created_at=faker.past_datetime(tzinfo=utc))


def test_encounters_ordered_by_created(as_practitioner):
    response = as_practitioner.get("/api/v1/ehr/encounters/?ordering=created_at")

    assert response[0]["createdAt"] < response[1]["createdAt"] < response[2]["createdAt"]
