import pytest


@pytest.fixture()
def practitioner(factory):
    return factory.practitioner()
