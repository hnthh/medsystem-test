from zoneinfo import ZoneInfo

import pytest
from django.utils import timezone


@pytest.fixture()
def assert_dt():
    def wrapper(dt_str, dt_obj):
        assert dt_str == timezone.localtime(dt_obj).strftime("%Y-%m-%dT%H:%M:%S")  # noqa: S101

    return wrapper


@pytest.fixture()
def utc() -> ZoneInfo:
    return ZoneInfo("UTC")
