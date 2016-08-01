from django.test import TestCase
from django.core.urlresolvers import reverse
from contacts.tests import factories


class ContactsTest(TestCase):
    def setUp(self):
        self.company = factories.CompanyFactory()
        self.person = factories.PersonFactory()
        self.email = factories.EmailAddressFactory(content_object=self.company)

    def testViewCompanyList(self):
        response = self.client.get(reverse('contacts_company_list'))
        self.failUnlessEqual(response.status_code, 200)

    def testViewCompanyDetail(self):
        response = self.client.get(self.company.get_absolute_url())
        self.failUnlessEqual(response.status_code, 200)

    def testViewPersonList(self):
        response = self.client.get(reverse('contacts_person_list'))
        self.failUnlessEqual(response.status_code, 200)

    def testViewPersonDetail(self):
        response = self.client.get(self.person.get_absolute_url())
        self.failUnlessEqual(response.status_code, 200)
