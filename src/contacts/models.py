from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericRelation

class Company(models.Model):
	"""Company model."""
	name = models.CharField(_('name'), max_length=200)
	nickname = models.CharField(_('nickname'), max_length=50, blank=True,
		null=True)
	slug = models.SlugField(_('slug'), max_length=50, unique=True)
	about = models.TextField(_('about'), blank=True, null=True)
	
	phone_number = GenericRelation('PhoneNumber')
	email_address = GenericRelation('EmailAddress')
	instant_messenger = GenericRelation('InstantMessenger')
	web_site = GenericRelation('WebSite')
	street_address = GenericRelation('StreetAddress')
	note = GenericRelation(Comment, object_id_field='object_pk')
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	class Meta:
		db_table = 'contacts_companies'
		ordering = ('name',)
		verbose_name = _('company')
		verbose_name_plural = _('companies')
	
	def __unicode__(self):
		return u"%s" % self.name
	
	@permalink
	def get_absolute_url(self):
		return ('contacts_company_detail', None, {
			'slug': self.slug,
		})
	
	@permalink
	def get_update_url(self):
		return ('contacts_company_update', None, {
			'slug': self.slug,
		})
	
	@permalink
	def get_delete_url(self):
		return ('contacts_company_delete', None, {
			'slug': self.slug,
		})

class Person(models.Model):
	"""Person model."""
	first_name = models.CharField(_('first name'), max_length=100)
	last_name = models.CharField(_('last name'), max_length=200)
	nickname = models.CharField(_('nickname'), max_length=100, blank=True,
		null=True)
	slug = models.SlugField(_('slug'), max_length=50, unique=True)
	title = models.CharField(_('title'), max_length=200, blank=True, null=True)
	company = models.ForeignKey(Company)
	about = models.TextField(_('about'), blank=True, null=True)
	
	user = models.ForeignKey(User, blank=True, null=True,
		verbose_name=_('user'))
	
	phone_number = GenericRelation('PhoneNumber')
	email_address = GenericRelation('EmailAddress')
	instant_messenger = GenericRelation('InstantMessenger')
	web_site = GenericRelation('WebSite')
	street_address = GenericRelation('StreetAddress')
	note = GenericRelation(Comment, object_id_field='object_pk')
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	class Meta:
		db_table = 'contacts_people'
		ordering = ('last_name', 'first_name')
		verbose_name = _('person')
		verbose_name_plural = _('people')
	
	def __unicode__(self):
		return self.fullname
	
	@property
	def fullname(self):
		return u"%s %s" % (self.first_name, self.last_name)
	
	@permalink
	def get_absolute_url(self):
		return ('contacts_person_detail', None, {
			'slug': self.slug,
		})
	
	@permalink
	def get_update_url(self):
		return ('contacts_person_update', None, {
			'slug': self.slug,
		})
	
	@permalink
	def get_delete_url(self):
		return ('contacts_person_delete', None, {
			'slug': self.slug,
		})

PHONE_LOCATION_CHOICIES = (
	('work', _('Work')),
	('mobile', _('Mobile')),
	('fax', _('Fax')),
	('pager', _('Pager')),
	('home', _('Home')),
	('other', _('Other')),
)

class PhoneNumber(models.Model):
	"""Phone Number model."""
	content_type = models.ForeignKey(ContentType,
		limit_choices_to={'app_label': 'contacts'})
	object_id = models.IntegerField(db_index=True)
	content_object = generic.GenericForeignKey()
	
	phone_number = models.CharField(_('number'), max_length=50)
	location = models.CharField(_('location'), max_length=6,
		choices=PHONE_LOCATION_CHOICIES, default='work')
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	def __unicode__(self):
		return u"%s (%s)" % (self.phone_number, self.location)
	
	class Meta:
		db_table = 'contacts_phone_numbers'
		verbose_name = 'phone number'
		verbose_name_plural = 'phone numbers'

LOCATION_CHOICES = (
	('work', _('Work')),
	('person', _('Personal')),
	('other', _('Other'))
)

class EmailAddress(models.Model):
	content_type = models.ForeignKey(ContentType,
		limit_choices_to={'app_label': 'contacts'})
	object_id = models.IntegerField(db_index=True)
	content_object = generic.GenericForeignKey()
	
	email_address = models.EmailField(_('email address'))
	location = models.CharField(_('location'), max_length=6,
		choices=LOCATION_CHOICES, default='work')
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	def __unicode__(self):
		return u"%s (%s)" % (self.email_address, self.location)
	
	class Meta:
		db_table = 'contacts_email_addresses'
		verbose_name = 'email address'
		verbose_name_plural = 'email addresses'

IM_SERVICE_CHOICES = (
	('aim', 'AIM'),
	('msn', 'MSN'),
	('icq', 'ICQ'),
	('jabber', 'Jabber'),
	('yahoo', 'Yahoo'),
	('skype', 'Skype'),
	('qq', 'QQ'),
	('sametime', 'Sametime'),
	('gadu-gadu', 'Gadu-Gadu'),
	('google-talk', 'Google Talk'),
	('other', _('Other'))
)

class InstantMessenger(models.Model):
	content_type = models.ForeignKey(ContentType,
		limit_choices_to={'app_label': 'contacts'})
	object_id = models.IntegerField(db_index=True)
	content_object = generic.GenericForeignKey()
	
	im_account = models.CharField(_('im account'), max_length=100)
	location = models.CharField(_('location'), max_length=6,
		choices=LOCATION_CHOICES, default='work')
	service = models.CharField(_('service'), max_length=11,
		choices=IM_SERVICE_CHOICES, default='jabber')
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	def __unicode__(self):
		return u"%s (%s)" % (self.im_account, self.location)
	
	class Meta:
		db_table = 'contacts_instant_messengers'
		verbose_name = 'instant messenger'
		verbose_name_plural = 'instant messengers'

class WebSite(models.Model):
	content_type = models.ForeignKey(ContentType,
		limit_choices_to={'app_label': 'contacts'})
	object_id = models.IntegerField(db_index=True)
	content_object = generic.GenericForeignKey()

	url = models.URLField(_('URL'))
	location = models.CharField(_('location'), max_length=6,
		choices=LOCATION_CHOICES, default='work')

	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	def __unicode__(self):
		return u"%s (%s)" % (self.url, self.location)
	
	class Meta:
		db_table = 'contacts_web_sites'
		verbose_name = _('web site')
		verbose_name_plural = _('web sites')
	
	def get_absolute_url(self):
		return u"%s?web_site=%s" % (self.content_object.get_absolute_url(), self.pk)

class StreetAddress(models.Model):
	content_type = models.ForeignKey(ContentType,
		limit_choices_to={'app_label': 'contacts'})
	object_id = models.IntegerField(db_index=True)
	content_object = generic.GenericForeignKey()
	
	street = models.TextField(_('street'), blank=True, null=True)
	city = models.CharField(_('city'), max_length=200, blank=True, null=True)
	province = models.CharField(_('province'), max_length=200, blank=True,
		null=True)
	postal_code = models.CharField(_('postal code'), max_length=10, blank=True,
		null=True)
	country = models.CharField(_('country'), max_length=100)
	location = models.CharField(_('location'), max_length=6,
		choices=LOCATION_CHOICES, default='work')
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	date_modified = models.DateTimeField(_('date modified'), auto_now=True)
	
	def __unicode__(self):
		return u"%s (%s)" % (self.city, self.location)
	
	class Meta:
		db_table = 'contacts_street_addresses'
		verbose_name = _('street address')
		verbose_name_plural = _('street addresses')
