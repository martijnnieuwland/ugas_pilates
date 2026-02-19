"""
Base settings for Uga's Pilates project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables depending on DJANGO_ENV
env_path = BASE_DIR / f".env.{os.getenv('DJANGO_ENV', 'dev')}"
load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.getenv("SECRET_KEY", "insecure-development-key")
GM_KEY = os.getenv("GM_KEY", "")
DEBUG = os.getenv("DEBUG") == "True"
ALLOWED_HOSTS = [host.strip() for host in os.getenv("ALLOWED_HOSTS", "").split(",") if host]

# Application definition
INSTALLED_APPS = [
    # Third-party apps
    "grappelli",
    "filebrowser",
    "tinymce",

    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",

    # Local apps
    "blog",
    "pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Databases
USE_CLOUD_SQL = os.environ.get("USE_CLOUD_SQL") == "true"

ROOT_URLCONF = "ugas_pilates.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ugas_pilates.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Brussels"
USE_I18N = True
USE_TZ = True

# Static and Media files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Filebrowser settings
FILEBROWSER_DIRECTORY = "uploads/"
FILEBROWSER_VERSIONS_BASEDIR = "_versions/"

# Grappelli
GRAPPELLI_ADMIN_TITLE = "Uga's Pilates Admin"

# TinyMCE
TINYMCE_DEFAULT_CONFIG = {
    "height": 360,
    "width": 800,
    "cleanup_on_startup": True,
    "custom_undo_redo_levels": 20,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
