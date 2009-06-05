import vobject
from django.template.defaultfilters import slugify

from contacts.models import Company, Person

def vcard(vcard, company):
	"""Imports a vcards into Django Contacts.
	
	:param vcard: A string of a vCard.
	:param type: string
	"""
	created = updated = []
	
	for card in vobject.readComponents(vcard):
		# Is it a Person
		if card.n.value.family and card.n.value.given:
			person, person_created = Person.objects.get_or_create(
				first_name=card.n.value.given,
				last_name=card.n.value.family,
				defaults = {
					'slug': slugify("%s %s" % (
						card.n.value.given, card.n.value.family)),
					'company': company,
				}
			)
			
			if person_created:
				created += [person,]
			else:
				updated += [person,]
	
	return created, updated