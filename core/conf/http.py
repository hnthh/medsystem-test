from core.conf.environ import env

ALLOWED_HOSTS = ["*"]

HOST = env("HOST", default=None)
