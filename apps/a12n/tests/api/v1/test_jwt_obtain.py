import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


url = "/api/v1/token/obtain/"


@pytest.fixture()
def user(user):
    user.set_password("password")
    user.save(update_fields=["password"])

    return user


@pytest.fixture()
def practitioner(practitioner, user):
    return practitioner.update(user=user)


@pytest.fixture()
def data(practitioner):
    return {
        "username": practitioner.user.username,
        "password": "password",
    }


@pytest.fixture()
def obtain(as_anon, data):
    return lambda data=data, status=status.HTTP_200_OK: as_anon.post(url, data=data, expected_status_code=status)


def test_access_not_granted_with_incorrect_password(data, obtain):
    data.update(password="incorrect-password")  # noqa: S106

    obtain(data=data, status=status.HTTP_401_UNAUTHORIZED)


def test_access_token_allows_access_ehr_urls(as_anon, obtain):
    access = obtain()["access"]
    as_anon.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

    as_anon.get("/api/v1/ehr/encounters/")
