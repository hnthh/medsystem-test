import pytest

from core.testing import FixtureFactory


@pytest.fixture()
def factory():
    return FixtureFactory()
