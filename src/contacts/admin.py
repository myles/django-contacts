from django.contrib import admin
from django.contrib.contenttypes.admin import (GenericTabularInline,
                                               GenericStackedInline)
from django_comments.models import Comment

from contacts import models


class EmailAddressInline(GenericTabularInline):
    model = models.EmailAddress


class PhoneNumberInline(GenericTabularInline):
    model = models.PhoneNumber


class InstantMessengerInline(GenericTabularInline):
    model = models.InstantMessenger


class WebSiteInline(GenericTabularInline):
    model = models.WebSite


class StreetAddressInline(GenericStackedInline):
    model = models.StreetAddress


class SpecialDateInline(GenericStackedInline):
    model = models.SpecialDate


class CommentInline(GenericStackedInline):
    model = Comment
    ct_fk_field = 'object_pk'


class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        PhoneNumberInline,
        EmailAddressInline,
        InstantMessengerInline,
        WebSiteInline,
        StreetAddressInline,
        SpecialDateInline,
        CommentInline,
    ]

    list_display = ('name',)
    search_fields = ['^name']
    prepopulated_fields = {'slug': ('name',)}


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        PhoneNumberInline,
        EmailAddressInline,
        InstantMessengerInline,
        WebSiteInline,
        StreetAddressInline,
        SpecialDateInline,
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
    search_fields = ['^name', '^about']
    prepopulated_fields = {'slug': ('name',)}


class LocationAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'date_modified')
    ordering = ('weight', 'name')
    search_fields = ['^name']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
            (None, {
                    'fields': (('name', 'slug',),)
            }),
            ('Advanced options', {
                    'fields': (('is_phone', 'is_street_address'),)
            })
    )

admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Location, LocationAdmin)
