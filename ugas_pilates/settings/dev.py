"""
Development settings for Uga's Pilates project.
"""

from .base import *

DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

# Debug Toolbar
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# Allow all hosts in dev
ALLOWED_HOSTS = ["*"]

# Easier local email handling (optional)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Local database settings - adjust as needed.  Currently set for Docker DB ugasdb_dev
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ugasdb",  # os.getenv("DB_NAME"),
        "USER": "mn",  # os.getenv("DB_USER"),
        "PASSWORD": "mn",  # os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": "5432",  # os.getenv("DB_PORT", "5432"),
    }
}
