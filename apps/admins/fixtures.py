import pytest


@pytest.fixture()
def admin(factory):
    return factory.admin()
