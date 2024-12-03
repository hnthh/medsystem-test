# fmt: off
pytest_plugins = [
    "apps.admins.factory",
    "apps.admins.fixtures",
    "apps.encounters.factory",
    "apps.encounters.fixtures",
    "apps.locations.factory",
    "apps.locations.fixtures",
    "apps.patients.factory",
    "apps.patients.fixtures",
    "apps.practitioners.factory",
    "apps.practitioners.fixtures",
    "apps.users.factory",
    "apps.users.fixtures",

    "core.factories",
    "core.fixtures",
]
# fmt: on
