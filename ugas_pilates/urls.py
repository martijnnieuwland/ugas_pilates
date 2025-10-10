"""
URL configuration for ugas_pilates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""

import sys

from . import views
from .sitemaps import StaticViewsSitemap

from debug_toolbar.toolbar import debug_toolbar_urls
from filebrowser.sites import site

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path


sitemaps = {
    "static": StaticViewsSitemap,
}

urlpatterns = [
    path("test/", views.testbed),
    path("admin/filebrowser/", site.urls),
    path("grappelli", include("grappelli.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("admin/", admin.site.urls, name="admin"),
    path("blog/", include("blog.urls")),
    path("", include("pages.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

# Conditionally add static URL patterns for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.TESTING:
    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
