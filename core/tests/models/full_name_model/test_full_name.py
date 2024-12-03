import pytest

from core.models import AppModelMixin, FullNameModel

pytestmark = pytest.mark.django_db


class Model(FullNameModel, AppModelMixin): ...


@pytest.fixture()
def model():
    return Model.objects.create()


@pytest.mark.parametrize(
    ("lname", "fname", "mname", "full_name"),
    [
        ("", "", "", ""),
        ("Фамилия", "", "", "Фамилия"),
        ("Фамилия", "Имя", "", "Фамилия Имя"),
        ("Фамилия", "Имя", "Отчество", "Фамилия Имя Отчество"),
    ],
)
def test_ok(fname, full_name, lname, mname, model):
    model.update(fname=fname, lname=lname, mname=mname)

    assert model.full_name == full_name
