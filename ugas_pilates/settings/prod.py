"""
Production settings for Uga's Pilates project.
"""

from .base import *

DEBUG = False

# Security best practices
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
CSRF_TRUSTED_ORIGINS = ["https://ugas-pilates-961565541630.europe-west1.run.app",
                        "https://ugaspilates-961565541630.europe-west1.run.app",
               "https://ugaspilates.com",
               "https://www.ugaspilates.com",
               "https://ugaspilates.be",
               "https://www.ugaspilates.be"
               ]

# Django
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = ["ugas-pilates-961565541630.europe-west1.run.app",
                 "ugaspilates-961565541630.europe-west1.run.app",
               "ugaspilates.com",
               "www.ugaspilates.com",
               "ugaspilates.be",
               "www.ugaspilates.be"
               ]

# CloudSQL database settings
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": DB_PASSWORD,
        "HOST": f"/cloudsql/{os.getenv('CLOUD_SQL_CONNECTION_NAME')}",
        "PORT": "5432",
    }
}

# Add any production-specific apps, middleware, or caching later
GM_KEY = os.getenv("GM_KEY", "")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE,  # Include base middleware
]

INSTALLED_APPS = [
    "storages",  # For Google Cloud Storage
    *INSTALLED_APPS,  # Include base apps
]

# Use GCS for Media files
# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'ugaspilates-media'
GS_DEFAULT_ACL = None  # This is the modern requirement for 'Uniform' buckets
GS_QUERYSTRING_AUTH = False  # Prevents long, messy signed URLs
GS_FILE_OVERWRITE = False     # Recommended: appends suffix if file exists
# GS_LOCATION = 'media'  # Optional: keeps files in a 'media/' folder in the bucket

# Use Whitenoise for Static files
# STATICFILES_STORAGE = "whitenoise.storage.StaticFilesStorage"
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": "ugaspilates-media",
            "default_acl": None,
            "querystring_auth": False,
            "file_overwrite": False,
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Keep these for URL generation
MEDIA_URL = 'https://storage.googleapis.com/ugaspilates-media/'

# Logging configuration for production
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
