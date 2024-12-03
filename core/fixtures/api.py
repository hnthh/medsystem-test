import pytest

from core.testing.api import DRFClient


@pytest.fixture()
def as_anon():
    return DRFClient()


@pytest.fixture()
def as_():
    def as_who(user):
        return DRFClient(user=user)

    return as_who


@pytest.fixture()
def as_admin(as_, admin):
    return as_(admin.user)


@pytest.fixture()
def as_patient(as_, patient):
    return as_(patient.user)


@pytest.fixture()
def as_practitioner(as_, practitioner):
    return as_(practitioner.user)
