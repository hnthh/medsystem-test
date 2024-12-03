from core.conf.environ import env

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="")

EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")

EMAIL_HOST = env("EMAIL_HOST", default="")

EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")

EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")

EMAIL_PORT = env("EMAIL_PORT", cast=int, default=587)

EMAIL_USE_TLS = env("EMAIL_USE_TLS", cast=bool, default=True)
