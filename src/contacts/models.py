from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericRelation
from contacts.managers import SpecialDateManager, CompanyManager, PersonManager



def get_primary_related_object(contact,related_object_name):
        """Determine and return the 'primary' related object."""
        related_object_manager = contact.__getattribute__(related_object_name)
        try: return related_object_manager.get(location__name="Work")
        except: pass
        try: return related_object_manager.get(location__name="Office")
        except: pass
        try: return related_object_manager.all()[0]
        except: pass
        return None


class Contact(models.Model):
        """ Unique attributes of former Company model."""
	name = models.CharField(_('name'), max_length=200, blank=True, null=True)
	logo = models.ImageField(_('photo'), upload_to='contacts/contacts/', blank=True, null=True)

        """ Unique attributes of former Person model."""
	first_name  = models.CharField(_('first name'), max_length=100, blank=True, null=True)
	last_name   = models.CharField(_('last name'), max_length=200, blank=True, null=True)
	middle_name = models.CharField(_('middle name'), max_length=200, blank=True, null=True)
	suffix      = models.CharField(_('suffix'), max_length=50, blank=True, null=True)
	title       = models.CharField(_('title'), max_length=200, blank=True)
	company     = models.ForeignKey('Contact', related_name='people', blank=True, null=True )
	user        = models.OneToOneField(User, blank=True, null=True,
                                           verbose_name=_('user'))
	photo = models.ImageField(_('photo'), upload_to='contacts/contacts/', blank=True, null=True)

        """ Common attributes of former Person and Company models."""
	nickname = models.CharField(_('nickname'), max_length=50, blank=True, null=True)
	slug     = models.SlugField(_('slug'), blank=True, max_length=50)
	about    = models.TextField(_('about'), blank=True)

	date_added    = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

        """ New attributes of combined model. """
	is_company = models.BooleanField(_('is company'), help_text="Only used for Company", default=False)
	prefix     = models.CharField(_('prefix'), max_length=50, blank=True, null=True)

	class Meta:
		db_table = 'contacts_contacts'
                #ordering = ('slug',)
		verbose_name = _('contact')
		verbose_name_plural = _('contacts')

        def __unicode__(self):
                return self.fullname

        @property
        def fullname(self):
                if self.is_company:
                        return u"%s" % self.name
                else:
                        return u"%s %s" % (self.first_name,self.last_name)

	@permalink
	def get_absolute_url(self):
		return ('contacts_contact_detail', None, {
                        'pk': self.pk,
			#'slug': self.slug,
		})

	@permalink
	def get_update_url(self):
		return ('contacts_contact_update', None, {
                        'pk': self.pk,
                        #'slug': self.slug,
		})

	@permalink
	def get_delete_url(self):
		return ('contacts_contact_delete', None, {
                        'pk': self.pk,
			#'slug': self.slug,
		})

        def primary_email_address(self):
                """Determine and return the 'primary' email address"""
                return get_primary_related_object(self,"email_address")

        def primary_phone_number(self):
                """Determine and return the 'primary' phone number"""
                return get_primary_related_object(self,"phone_number")

        def primary_street_address(self):
                """Determine and return the 'primary' street address"""
                return get_primary_related_object(self,"street_address")

        def primary_website(self):
                """Determine and return the 'primary' website"""
                return get_primary_related_object(self,"web_site")


class Company(Contact):
	"""Company model."""
	objects = CompanyManager()

	class Meta:
		proxy = True
		ordering = ('name',)
                verbose_name = _('company')
                verbose_name_plural = _('companies')

	def __init__(self, *args, **kwargs):
		# Call Contact's super and set is_company to True
		super(Contact,self).__init__(*args,**kwargs)
		self.is_company = True

	@permalink
	def get_absolute_url(self):
		return ('contacts_company_detail', None, {
			'pk': self.pk,
			#'slug': self.slug,
		})

	@permalink
	def get_update_url(self):
		return ('contacts_company_update', None, {
			'pk': self.pk,
			#'slug': self.slug,
		})

	@permalink
	def get_delete_url(self):
		return ('contacts_company_delete', None, {
			'pk': self.pk,
			#'slug': self.slug,
		})


class Person(Contact):
	"""Person model."""
	objects = PersonManager()

	class Meta:
		proxy = True
		ordering = ('last_name', 'first_name')
                verbose_name = _('person')
                verbose_name_plural = _('people')

	def __init__(self, *args, **kwargs):
		# Call Contact's super
		super(Contact,self).__init__(*args,**kwargs)

	@property
	def fullname(self):
		return u"%s %s %s %s" % (self.first_name, self.middle_name, self.last_name, self.suffix)

	@permalink
	def get_absolute_url(self):
		return ('contacts_person_detail', None, {
			'pk': self.pk,
			#'slug': self.slug,
		})

	@permalink
	def get_update_url(self):
		return ('contacts_person_update', None, {
			'pk': self.pk,
			#'slug': self.slug,
		})

	@permalink
	def get_delete_url(self):
		return ('contacts_person_delete', None, {
			'pk': self.pk,
			#'slug': self.slug,
		})


class Group(models.Model):
	"""Group model."""
	name = models.CharField(_('name'), max_length=200)
	slug = models.SlugField(_('slug'), blank=True,max_length=50)
	about = models.TextField(_('about'), blank=True)

	people = models.ManyToManyField(Person, verbose_name='people', blank=True,
		null=True)
	companies = models.ManyToManyField(Company, verbose_name='companies',
		blank=True, null=True)

	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

	class Meta:
		db_table = 'contacts_groups'
		ordering = ('name',)
		verbose_name = _('group')
		verbose_name_plural = _('groups')

	def __unicode__(self):
		return u"%s" % self.name

	@permalink
	def get_absolute_url(self):
		return ('contacts_group_detail', None, {
                        'pk': self.pk,
			#'slug': self.slug,
                })

	@permalink
	def get_update_url(self):
		return ('contacts_group_update', None, {
                        'pk': self.pk,
			#'slug': self.slug,
		})

	@permalink
	def get_delete_url(self):
		return ('contacts_group_delete', None, {
                        'pk': self.pk,
			#'slug': self.slug,
		})

class Location(models.Model):
	"""Location model."""
	WEIGHT_CHOICES = [(i,i) for i in range(11)]

	name = models.CharField(_('name'), max_length=200)
	slug = models.SlugField(_('slug'), blank=True, max_length=50)

	is_phone = models.BooleanField(_('is phone'), help_text="Only used for Phone", default=False)
	is_street_address = models.BooleanField(_('is street address'), help_text="Only used for Street Address", default=False)

	weight = models.IntegerField(max_length=2, choices=WEIGHT_CHOICES, default=0)

	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

	def __unicode__(self):
		return u"%s" % (self.name)

	class Meta:
		db_table = 'contacts_locations'
		ordering = ('weight',)
		verbose_name = _('location')
		verbose_name_plural = _('locations')

class PhoneNumber(models.Model):
	"""Phone Number model."""
	contact = models.ForeignKey(Contact, related_name='phone_number')

	phone_number = models.CharField(_('number'), max_length=50)
	location = models.ForeignKey(Location, limit_choices_to={'is_street_address': False})

	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

	def __init__(self, *args, **kwargs):
		# If there is a content_object in the kwarguments, peel it off into
		# a variable named content_object_value
		if 'content_object' in kwargs:
			content_object_value = kwargs['content_object']
			del kwargs['content_object']

		# Then run the normal init
		super(PhoneNumber,self).__init__(*args,**kwargs)
		if 'content_object_value' in locals():
			self.contact = content_object_value

	def __unicode__(self):
		return u"%s (%s)" % (self.phone_number, self.location)

	class Meta:
		db_table = 'contacts_phone_numbers'
		verbose_name = 'phone number'
		verbose_name_plural = 'phone numbers'

class EmailAddress(models.Model):
	contact = models.ForeignKey(Contact, related_name='email_address')

	email_address = models.EmailField(_('email address'))
	location = models.ForeignKey(Location, limit_choices_to={'is_street_address': False, 'is_phone': False})

	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

        def __init__(self, *args, **kwargs):
                # If there is a content_object in the kwarguments, peel it off into
                # a variable named content_object_value
                if 'content_object' in kwargs:
                        content_object_value = kwargs['content_object']
                        del kwargs['content_object']

                # Then run the normal init
                super(EmailAddress,self).__init__(*args,**kwargs)
                if 'content_object_value' in locals():
                        self.contact = content_object_value

	def __unicode__(self):
		return u"%s (%s)" % (self.email_address, self.location)

	class Meta:
		db_table = 'contacts_email_addresses'
		verbose_name = 'email address'
		verbose_name_plural = 'email addresses'

class InstantMessenger(models.Model):
	OTHER = 'other'

	IM_SERVICE_CHOICES = (
		('aim', _('AIM')),
		('msn', _('MSN')),
		('icq', _('ICQ')),
		('jabber', _('Jabber')),
		('yahoo', _('Yahoo')),
		('skype', _('Skype')),
		('qq', _('QQ')),
		('sametime', _('Sametime')),
		('gadu-gadu', _('Gadu-Gadu')),
		('google-talk', _('Google Talk')),
		(OTHER, _('Other'))
	)

	contact = models.ForeignKey(Contact, related_name='instant_messenger')

	im_account = models.CharField(_('im account'), max_length=100)
	location = models.ForeignKey(Location, limit_choices_to={'is_street_address': False, 'is_phone': False})
	service = models.CharField(_('service'), max_length=11,
		choices=IM_SERVICE_CHOICES, default=OTHER)

	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

        def __init__(self, *args, **kwargs):
                # If there is a content_object in the kwarguments, peel it off into
                # a variable named content_object_value
                if 'content_object' in kwargs:
                        content_object_value = kwargs['content_object']
                        del kwargs['content_object']

                # Then run the normal init
                super(InstantMessenger,self).__init__(*args,**kwargs)
                if 'content_object_value' in locals():
                        self.contact = content_object_value

	def __unicode__(self):
		return u"%s (%s)" % (self.im_account, self.location)

	class Meta:
		db_table = 'contacts_instant_messengers'
		verbose_name = 'instant messenger'
		verbose_name_plural = 'instant messengers'

class WebSite(models.Model):
	contact = models.ForeignKey(Contact, related_name='web_site')

	url = models.URLField(_('URL'))
	location = models.ForeignKey(Location, limit_choices_to={'is_street_address': False, 'is_phone': False})

	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

        def __init__(self, *args, **kwargs):
                # If there is a content_object in the kwarguments, peel it off into
                # a variable named content_object_value
                if 'content_object' in kwargs:
                        content_object_value = kwargs['content_object']
                        del kwargs['content_object']

                # Then run the normal init
                super(WebSite,self).__init__(*args,**kwargs)
                if 'content_object_value' in locals():
                        self.contact = content_object_value

	def __unicode__(self):
		return u"%s (%s)" % (self.url, self.location)

	class Meta:
		db_table = 'contacts_web_sites'
		verbose_name = _('web site')
		verbose_name_plural = _('web sites')

	def get_absolute_url(self):
		return u"%s?web_site=%s" % (self.content_object.get_absolute_url(), self.pk)

class StreetAddress(models.Model):
	contact = models.ForeignKey(Contact, related_name='street_address')

	street = models.TextField(_('street'), blank=True)
	street2 = models.TextField(_('street2'), blank=True)
	city = models.CharField(_('city'), max_length=200, blank=True)
	province = models.CharField(_('province'), max_length=200, blank=True)
	postal_code = models.CharField(_('postal code'), max_length=10, blank=True)
	country = models.CharField(_('country'), max_length=100)
	location = models.ForeignKey(Location, limit_choices_to={'is_phone': False})

	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

        def __init__(self, *args, **kwargs):
                # If there is a content_object in the kwarguments, peel it off into
                # a variable named content_object_value
                if 'content_object' in kwargs:
                        content_object_value = kwargs['content_object']
                        del kwargs['content_object']

                # Then run the normal init
                super(StreetAddress,self).__init__(*args,**kwargs)
                if 'content_object_value' in locals():
                        self.contact = content_object_value

	def __unicode__(self):
		return u"%s (%s)" % (self.city, self.location)

	class Meta:
		db_table = 'contacts_street_addresses'
		verbose_name = _('street address')
		verbose_name_plural = _('street addresses')

class SpecialDate(models.Model):
	contact = models.ForeignKey(Contact, related_name="special_date")
	# object_id = models.IntegerField(db_index=True)
	# content_object = generic.GenericForeignKey()

	occasion = models.TextField(_('occasion'), max_length=200)
	date = models.DateField(_('date'))
	every_year = models.BooleanField(_('every year'), default=True)

	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)

	objects = SpecialDateManager()

        def __init__(self, *args, **kwargs):
                # If there is a content_object in the kwarguments, peel it off into
                # a variable named content_object_value
                if 'content_object' in kwargs:
                        content_object_value = kwargs['content_object']
                        del kwargs['content_object']

                # Then run the normal init
                super(SpecialDate,self).__init__(*args,**kwargs)
                if 'content_object_value' in locals():
                        self.contact = content_object_value

	def __unicode__(self):
		return u"%s: %s" % (self.occasion, self.date)

	class Meta:
		db_table = 'contacts_special_dates'
		verbose_name = _('special date')
		verbose_name_plural = _('special dates')
