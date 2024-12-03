import pytest


@pytest.fixture()
def encounter(factory):
    return factory.encounter()
