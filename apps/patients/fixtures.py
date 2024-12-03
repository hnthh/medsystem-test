import pytest


@pytest.fixture()
def patient(factory):
    return factory.patient(phone=factory.phone_number())
