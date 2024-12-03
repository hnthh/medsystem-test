import pytest

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.freeze_time("2032-01-07"),
]

url = "/api/v1/ehr/encounters/"


@pytest.fixture(autouse=True)
def encounter(factory):
    return factory.encounter()


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ("2032-01-06", 1),
        ("2032-01-07", 1),
        ("2032-01-08", 0),
    ],
)
def test_response_filtered_by_created_after(as_practitioner, expected, query):
    response = as_practitioner.get(f"{url}?created_at_after={query}")

    assert len(response) == expected


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ("2032-01-06", 0),
        ("2032-01-07", 0),
        ("2032-01-08", 1),
    ],
)
def test_response_filtered_by_created_before(as_practitioner, expected, query):
    response = as_practitioner.get(f"{url}?created_at_before={query}")

    assert len(response) == expected
