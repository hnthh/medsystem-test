from split_settings.tools import include

from core.conf.environ import env

include("conf/*.py")

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)
