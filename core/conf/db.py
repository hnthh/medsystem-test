from core.conf.environ import env

DATABASES = {
    "default": env.db(),
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
