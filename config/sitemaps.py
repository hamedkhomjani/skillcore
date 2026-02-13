from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['pricing:home', 'pages:about', 'pages:contact', 'pages:terms', 'pages:privacy']

    def location(self, item):
        return reverse(item)
