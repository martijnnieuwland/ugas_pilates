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
