# fmt: off
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "corsheaders",
    "phonenumber_field",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",

    "core",
    "apps.a12n.apps.A12nConfig",
    "apps.admins.apps.AdminsConfig",
    "apps.encounters.apps.EncountersConfig",
    "apps.locations.apps.LocationsConfig",
    "apps.patients.apps.PatientsConfig",
    "apps.practitioners.apps.PractitionersConfig",
    "apps.users.apps.UsersConfig",
]
