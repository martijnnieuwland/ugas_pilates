import os

# Default to base, but allow override via environment variable
DJANGO_ENV = os.getenv("DJANGO_ENV", "development")

if DJANGO_ENV == "production":
    from .prod import *
else:
    from .dev import *
