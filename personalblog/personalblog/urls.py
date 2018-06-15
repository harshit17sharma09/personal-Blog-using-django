from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import PostSitemap


sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [
    url('admin/', admin.site.urls),
    url('main/', include('main.urls', namespace='main')),
    url('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]