from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
import dbindexer
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ParkToGo.views.home', name='home'),
    url(r'^parktogo/', include('mainpage.urls', namespace = 'mainpage')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
