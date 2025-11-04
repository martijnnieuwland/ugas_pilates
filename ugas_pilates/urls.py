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

from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .sitemaps import StaticViewsSitemap
from filebrowser.sites import site

from ugas_pilates.admin import custom_admin_site


if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar


sitemaps = {
    "static": StaticViewsSitemap,
}

urlpatterns = [
    path("admin/filebrowser/", site.urls),
    path("grappelli/", include("grappelli.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("admin/", custom_admin_site.urls, name="admin"),
    path("blog/", include("blog.urls")),
    path("", include("pages.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

# Conditionally add static and debug_toolbar URL patterns for development
if settings.DEBUG:
    # Serve static/media in dev

    urlpatterns = staticfiles_urlpatterns() + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Debug toolbar
    if "debug_toolbar" in settings.INSTALLED_APPS:
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
