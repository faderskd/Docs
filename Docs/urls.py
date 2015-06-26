from django.conf.urls import patterns, include, url
from api import urls
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(urls, namespace='api')),
)
