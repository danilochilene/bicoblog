from django.conf.urls.defaults import *
from .views import index
from .models import Entry, LatestEntriesFeed
from django.conf.urls import patterns, include, url
from .feeds import LastEntries

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    (r'^latest/feed/$', LatestEntriesFeed()), 
    (r'^entry/(?P<entry_id>\d+)/$', 'bicoblog.blog.views.entry'),
    (r'^contact/$', 'views.contact'),
)