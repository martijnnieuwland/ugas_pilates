from django.contrib import sitemaps
from django.urls import reverse

class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ['home', 'studio', 'instructors', 'testimonials', 'faq', 'blog',
                'schedule', 'pricing', 'contact', 'privacy', 'terms']

    def location(self, item):
        return reverse(item)
