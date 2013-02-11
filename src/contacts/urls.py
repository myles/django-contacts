try:
    from django.conf.urls import *
except:
    from django.conf.urls.defaults import *

urlpatterns = patterns('contacts.views',
	url(r'^companies/page/(?P<page>\d+)/$',
		view = 'company.list',
		name = 'contacts_company_list_paginated',
	),
	url(r'^companies/add/$',
		view = 'company.create',
		name = 'contacts_company_create',
	),
	url(r'^companies/(?P<pk>\d+)-(?P<slug>[-\w]+)/delete/$',
		view = 'company.delete',
		name = 'contacts_company_delete'
	),
	url(r'^companies/(?P<pk>\d+)/delete/$',
		view = 'company.delete',
		name = 'contacts_company_delete'
	),
	url(r'^companies/(?P<pk>\d+)-(?P<slug>[-\w]+)/edit/$',
		view = 'company.update',
		name = 'contacts_company_update'
	),
	url(r'^companies/(?P<pk>\d+)/edit/$',
		view = 'company.update',
		name = 'contacts_company_update'
	),
	url(r'^companies/(?P<pk>\d+)-(?P<slug>[-\w]+)/$',
		view = 'company.detail',
		name = 'contacts_company_detail'
	),
	url(r'^companies/(?P<pk>\d+)/$',
		view = 'company.detail',
		name = 'contacts_company_detail'
	),
	url(r'^companies/$',
		view = 'company.list',
		name = 'contacts_company_list',
	),

	url(r'^people/page/(?P<page>\d+)/$',
		view = 'person.list',
		name = 'contacts_person_list_paginated',
	),
	url(r'^people/add/$',
		view = 'person.create',
		name = 'contacts_person_create',
	),
	url(r'^people/(?P<pk>\d+)-(?P<slug>[-\w]+)/delete/$',
		view = 'person.delete',
		name = 'contacts_person_delete'
	),
	url(r'^people/(?P<pk>\d+)/delete/$',
		view = 'person.delete',
		name = 'contacts_person_delete'
	),
	url(r'^people/(?P<pk>\d+)-(?P<slug>[-\w]+)/edit/$',
		view = 'person.update',
		name = 'contacts_person_update'
	),
	url(r'^people/(?P<pk>\d+)/edit/$',
		view = 'person.update',
		name = 'contacts_person_update'
	),
	url(r'^people/(?P<pk>\d+)-(?P<slug>[-\w]+)/$',
		view = 'person.detail',
		name = 'contacts_person_detail',
	),
	url(r'^people/(?P<pk>\d+)/$',
		view = 'person.detail',
		name = 'contacts_person_detail',
	),
	url(r'^people/$',
		view = 'person.list',
		name = 'contacts_person_list',
	),

	url(r'^groups/page/(?P<page>\d+)/$',
		view = 'group.list',
		name = 'contacts_group_list_paginated',
	),
	url(r'^groups/add/$',
		view = 'group.create',
		name = 'contacts_group_create',
	),
	url(r'^groups/(?P<pk>\d+)-(?P<slug>[-\w]+)/delete/$',
		view = 'group.delete',
		name = 'contacts_group_delete'
	),
	url(r'^groups/(?P<pk>\d+)/delete/$',
		view = 'group.delete',
		name = 'contacts_group_delete'
	),
	url(r'^groups/(?P<pk>\d+)-(?P<slug>[-\w]+)/edit/$',
		view = 'group.update',
		name = 'contacts_group_update'
	),
	url(r'^groups/(?P<pk>\d+)/edit/$',
		view = 'group.update',
		name = 'contacts_group_update'
	),
	url(r'^groups/(?P<pk>\d+)-(?P<slug>[-\w]+)/$',
		view = 'group.detail',
		name = 'contacts_group_detail',
	),
	url(r'^groups/(?P<pk>\d+)/$',
		view = 'group.detail',
		name = 'contacts_group_detail',
	),
	url(r'^groups/$',
		view = 'group.list',
		name = 'contacts_group_list'
	),
)
