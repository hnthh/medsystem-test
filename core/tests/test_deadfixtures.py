import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.usefixtures("admin", "as_admin", "as_patient", "user")
def test_deadfixtures(): ...
