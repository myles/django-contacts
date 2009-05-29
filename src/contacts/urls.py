from django.conf.urls.defaults import *

urlpatterns = patterns('contacts.views',
	url(r'^companies/(?P<slug>[-\w]+)/$',
		view = 'company_detail',
		name = 'contacts_company_detail'
	),
	url(r'^companies/page/(?P<page>\d+)/$',
		view = 'company_list',
		name = 'contacts_company_list_paginated',
	),
	url(r'^companies/$',
		view = 'company_list',
		name = 'contacts_company_list',
	),
	url(r'^people/(?P<slug>[-\w]+)/$',
		view = 'person_detail',
		name = 'contacts_person_detail'
	),
	url(r'^people/page/(?P<page>\d+)/$',
		view = 'person_list',
		name = 'contacts_person_list_paginated',
	),
	url(r'^people/$',
		view = 'person_list',
		name = 'contacts_person_list',
	),
)