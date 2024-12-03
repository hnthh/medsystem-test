import pytest


@pytest.fixture()
def location(factory):
    return factory.location()
