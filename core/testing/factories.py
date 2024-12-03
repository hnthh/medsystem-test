from collections.abc import Callable
from functools import partial
from typing import ClassVar

from faker import Faker
from mixer.backend.django import mixer


def register(method):
    name = method.__name__
    FixtureRegistry.METHODS[name] = method
    return method


class FixtureRegistry:
    METHODS: ClassVar[dict[str, Callable]] = {}

    def get(self, name: str) -> Callable:
        method = self.METHODS.get(name)
        if not method:
            msg = f"Factory method “{name}” not found."

            raise AttributeError(msg)

        return method


class CycleFixtureFactory:
    def __init__(self, factory, count):
        self.count = count
        self.factory = factory

    def __getattr__(self, name):
        if hasattr(self.factory, name):
            return lambda *args, **kwargs: [getattr(self.factory, name)(*args, **kwargs) for _ in range(self.count)]

        return None


class FixtureFactory:
    def __init__(self):
        self.mixer = mixer
        self.registry = FixtureRegistry()

    @property
    def faker(self):
        return Faker()

    def __getattr__(self, name):
        method = self.registry.get(name)
        return partial(method, self)

    def cycle(self, count):
        return CycleFixtureFactory(self, count)
