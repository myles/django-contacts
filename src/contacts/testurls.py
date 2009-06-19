from django.contrib import admin
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/(.*)', admin.site.root),
	url(r'^comments/', include('django.contrib.comments.urls')),
	
	url(r'^', include('contacts.urls')),
)
