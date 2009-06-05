from django.test import TestCase

from contacts.models import Company, Person

class ContactsTest(TestCase):
	fixtures = ['contacts',]
	urls = 'contacts.testurls'
	
	company_miys = Company.objects.get(pk=1)
	person_mb = Person.objects.get(pk=1)
	
	def setUp(self):
		email = self.company_miys.email_address.create()
		email.email_address = 'info@monkeyinyoursoul.com'
		email.location = 'work'
		email.save()
	
	def testEmailAddressThoughCompany(self):
		email = self.company_miys.email_address.get()
		self.failUnlessEqual(email.email_address, 'info@monkeyinyoursoul.com')
	
	def testViewCompanyList(self):
		response = self.client.get('/contacts/companies/')
		self.failUnlessEqual(response.status_code, 200)
	
	def testViewCompanyDetail(self):
		response = self.client.get(self.company_miys.get_absolute_url())
		self.failUnlessEqual(response.status_code, 200)
	
	def testViewPersonList(self):
		response = self.client.get('/contacts/people/')
		self.failUnlessEqual(response.status_code, 200)
	
	def testViewPersonDetail(self):
		response = self.client.get(self.person_mb.get_absolute_url())
		self.failUnlessEqual(response.status_code, 200)