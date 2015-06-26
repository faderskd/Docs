from api.views import ContactView,  AuthorListView, AuthorDetail

__author__ = 'daniel'

from django.conf.urls import patterns, include, url, handler404


urlpatterns = [
    url(r'^success/$', ContactView.as_view(), name='success'),
    url(r'^author-details/(?P<pk>[0-9]+)$', AuthorDetail.as_view(), name='author-details'),
    url(r'^author-list/(?P<pk>[0-9]+)$', AuthorListView.as_view(), name='author-list'),
]