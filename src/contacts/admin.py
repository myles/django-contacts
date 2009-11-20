from django.contrib import admin
from django.contrib.contenttypes import generic
from django.contrib.comments.models import Comment

from contacts.models import Company, Person, Group, PhoneNumber, EmailAddress, InstantMessenger, WebSite, StreetAddress

class EmailAddressInline(generic.GenericTabularInline):
	model = EmailAddress

class PhoneNumberInline(generic.GenericTabularInline):
	model = PhoneNumber

class InstantMessengerInline(generic.GenericTabularInline):
	model = InstantMessenger

class WebSiteInline(generic.GenericTabularInline):
	model = WebSite

class StreetAddressInline(generic.GenericStackedInline):
	model = StreetAddress

class CommentInline(generic.GenericStackedInline):
	model = Comment
	ct_fk_field = 'object_pk'

class CompanyAdmin(admin.ModelAdmin):
	inlines = [
		PhoneNumberInline,
		EmailAddressInline,
		InstantMessengerInline,
		WebSiteInline,
		StreetAddressInline,
		CommentInline,
	]
	
	list_display = ('name',)
	search_fields = ['^name',]
	prepopulated_fields = {'slug': ('name',)}

class PersonAdmin(admin.ModelAdmin):
	inlines = [
		PhoneNumberInline,
		EmailAddressInline,
		InstantMessengerInline,
		WebSiteInline,
		StreetAddressInline,
		CommentInline,
	]
	
	list_display_links = ('first_name', 'last_name',)
	list_display = ('first_name', 'last_name', 'company',)
	list_filter = ('company',)
	ordering = ('last_name', 'first_name')
	search_fields = ['^first_name', '^last_name', '^company__name']
	prepopulated_fields = {'slug': ('first_name', 'last_name')}

class GroupAdmin(admin.ModelAdmin):
	list_display_links = ('name',)
	list_display = ('name', 'date_modified')
	ordering = ('-date_modified', 'name',)
	search_fields = ['^name', '^about',]
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Company, CompanyAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)