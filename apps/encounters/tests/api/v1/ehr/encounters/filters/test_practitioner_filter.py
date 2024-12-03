import pytest

pytestmark = pytest.mark.django_db


url = "/api/v1/ehr/encounters/"


@pytest.fixture()
def practitioner(practitioner):
    return practitioner.update(fname="Имя", lname="Фамилия", mname="Отчество")


@pytest.fixture()
def encounter(encounter, practitioner):
    return encounter.update(practitioner=practitioner)


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ("Фамилия Имя Отчество", 1),
        ("фамилия имя отчество", 1),
        ("имя", 1),
        ("   фамилия   ", 1),
        ("mimokrokodil", 0),
    ],
)
@pytest.mark.usefixtures("encounter")
def test_response_filtered_by_practitioner(as_practitioner, expected, query):
    response = as_practitioner.get(f"{url}?practitioner={query}")

    assert len(response) == expected
