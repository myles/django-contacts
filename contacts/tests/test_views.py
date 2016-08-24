from django.test import TestCase
from django.core.urlresolvers import reverse_lazy as reverse
from contacts.tests import factories
from contacts import models

COMPANY_UPDATE_POST = {
   'contacts-emailaddress-content_type-object_id-0-email_address': '',
   'contacts-emailaddress-content_type-object_id-0-id': '',
   'contacts-emailaddress-content_type-object_id-0-location': '',
   'contacts-emailaddress-content_type-object_id-INITIAL_FORMS': '0',
   'contacts-emailaddress-content_type-object_id-MAX_NUM_FORMS': '1000',
   'contacts-emailaddress-content_type-object_id-MIN_NUM_FORMS': '0',
   'contacts-emailaddress-content_type-object_id-TOTAL_FORMS': '1',
   'contacts-instantmessenger-content_type-object_id-0-id': '',
   'contacts-instantmessenger-content_type-object_id-0-im_account': '',
   'contacts-instantmessenger-content_type-object_id-0-location': '',
   'contacts-instantmessenger-content_type-object_id-0-service': 'other',
   'contacts-instantmessenger-content_type-object_id-INITIAL_FORMS': '0',
   'contacts-instantmessenger-content_type-object_id-MAX_NUM_FORMS': '1000',
   'contacts-instantmessenger-content_type-object_id-MIN_NUM_FORMS': '0',
   'contacts-instantmessenger-content_type-object_id-TOTAL_FORMS': '1',
   'contacts-phonenumber-content_type-object_id-0-id': '',
   'contacts-phonenumber-content_type-object_id-0-location': '',
   'contacts-phonenumber-content_type-object_id-0-phone_number': '',
   'contacts-phonenumber-content_type-object_id-INITIAL_FORMS': '0',
   'contacts-phonenumber-content_type-object_id-MAX_NUM_FORMS': '1000',
   'contacts-phonenumber-content_type-object_id-MIN_NUM_FORMS': '0',
   'contacts-phonenumber-content_type-object_id-TOTAL_FORMS': '1',
   'contacts-specialdate-content_type-object_id-0-date': '',
   'contacts-specialdate-content_type-object_id-0-every_year': 'on',
   'contacts-specialdate-content_type-object_id-0-id': '',
   'contacts-specialdate-content_type-object_id-0-occasion': '',
   'contacts-specialdate-content_type-object_id-INITIAL_FORMS': '0',
   'contacts-specialdate-content_type-object_id-MAX_NUM_FORMS': '1000',
   'contacts-specialdate-content_type-object_id-MIN_NUM_FORMS': '0',
   'contacts-specialdate-content_type-object_id-TOTAL_FORMS': '1',
   'contacts-streetaddress-content_type-object_id-0-city': '',
   'contacts-streetaddress-content_type-object_id-0-country': '',
   'contacts-streetaddress-content_type-object_id-0-id': '',
   'contacts-streetaddress-content_type-object_id-0-location': '',
   'contacts-streetaddress-content_type-object_id-0-postal_code': '',
   'contacts-streetaddress-content_type-object_id-0-province': '',
   'contacts-streetaddress-content_type-object_id-0-street': '',
   'contacts-streetaddress-content_type-object_id-INITIAL_FORMS': '0',
   'contacts-streetaddress-content_type-object_id-MAX_NUM_FORMS': '1000',
   'contacts-streetaddress-content_type-object_id-MIN_NUM_FORMS': '0',
   'contacts-streetaddress-content_type-object_id-TOTAL_FORMS': '1',
   'contacts-website-content_type-object_id-0-id': '',
   'contacts-website-content_type-object_id-0-location': '',
   'contacts-website-content_type-object_id-0-url': '',
   'contacts-website-content_type-object_id-INITIAL_FORMS': '0',
   'contacts-website-content_type-object_id-MAX_NUM_FORMS': '1000',
   'contacts-website-content_type-object_id-MIN_NUM_FORMS': '0',
   'contacts-website-content_type-object_id-TOTAL_FORMS': '1',
   'name': 'Foo Inc.',
   'slug': 'foo',
}
PERSON_UPDATE_POST = {
    'company': '',
    'contacts-emailaddress-content_type-object_id-0-email_address': '',
    'contacts-emailaddress-content_type-object_id-0-id': '',
    'contacts-emailaddress-content_type-object_id-0-location': '',
    'contacts-emailaddress-content_type-object_id-INITIAL_FORMS': '0',
    'contacts-emailaddress-content_type-object_id-MAX_NUM_FORMS': '1000',
    'contacts-emailaddress-content_type-object_id-MIN_NUM_FORMS': '0',
    'contacts-emailaddress-content_type-object_id-TOTAL_FORMS': '1',
    'contacts-instantmessenger-content_type-object_id-0-id': '',
    'contacts-instantmessenger-content_type-object_id-0-im_account': '',
    'contacts-instantmessenger-content_type-object_id-0-location': '',
    'contacts-instantmessenger-content_type-object_id-0-service': 'other',
    'contacts-instantmessenger-content_type-object_id-INITIAL_FORMS': '0',
    'contacts-instantmessenger-content_type-object_id-MAX_NUM_FORMS': '1000',
    'contacts-instantmessenger-content_type-object_id-MIN_NUM_FORMS': '0',
    'contacts-instantmessenger-content_type-object_id-TOTAL_FORMS': '1',
    'contacts-phonenumber-content_type-object_id-0-id': '',
    'contacts-phonenumber-content_type-object_id-0-location': '',
    'contacts-phonenumber-content_type-object_id-0-phone_number': '',
    'contacts-phonenumber-content_type-object_id-INITIAL_FORMS': '0',
    'contacts-phonenumber-content_type-object_id-MAX_NUM_FORMS': '1000',
    'contacts-phonenumber-content_type-object_id-MIN_NUM_FORMS': '0',
    'contacts-phonenumber-content_type-object_id-TOTAL_FORMS': '1',
    'contacts-specialdate-content_type-object_id-0-date': '',
    'contacts-specialdate-content_type-object_id-0-every_year': 'on',
    'contacts-specialdate-content_type-object_id-0-id': '',
    'contacts-specialdate-content_type-object_id-0-occasion': '',
    'contacts-specialdate-content_type-object_id-INITIAL_FORMS': '0',
    'contacts-specialdate-content_type-object_id-MAX_NUM_FORMS': '1000',
    'contacts-specialdate-content_type-object_id-MIN_NUM_FORMS': '0',
    'contacts-specialdate-content_type-object_id-TOTAL_FORMS': '1',
    'contacts-streetaddress-content_type-object_id-0-city': '',
    'contacts-streetaddress-content_type-object_id-0-country': '',
    'contacts-streetaddress-content_type-object_id-0-id': '',
    'contacts-streetaddress-content_type-object_id-0-location': '',
    'contacts-streetaddress-content_type-object_id-0-postal_code': '',
    'contacts-streetaddress-content_type-object_id-0-province': '',
    'contacts-streetaddress-content_type-object_id-0-street': '',
    'contacts-streetaddress-content_type-object_id-INITIAL_FORMS': '0',
    'contacts-streetaddress-content_type-object_id-MAX_NUM_FORMS': '1000',
    'contacts-streetaddress-content_type-object_id-MIN_NUM_FORMS': '0',
    'contacts-streetaddress-content_type-object_id-TOTAL_FORMS': '1',
    'contacts-website-content_type-object_id-0-id': '',
    'contacts-website-content_type-object_id-0-location': '',
    'contacts-website-content_type-object_id-0-url': '',
    'contacts-website-content_type-object_id-INITIAL_FORMS': '0',
    'contacts-website-content_type-object_id-MAX_NUM_FORMS': '1000',
    'contacts-website-content_type-object_id-MIN_NUM_FORMS': '0',
    'contacts-website-content_type-object_id-TOTAL_FORMS': '1',
    'first_name': 'Joe',
    'last_name': 'LeTaxi',
    'title': ''
}


class CompanyListTest(TestCase):
    url = reverse('contacts_company_list')

    def test_view(self):
        factories.CompanyFactory.build_batch(25)
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 200)

    def test_empty(self):
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 200)

    def test_paginated(self):
        factories.CompanyFactory.build_batch(25)
        url = reverse('contacts_company_list_paginated', kwargs={'page': 1})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_no_previous_and_no_next(self):
        factories.CompanyFactory.build_batch(5)
        url = reverse('contacts_company_list_paginated', kwargs={'page': 1})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_invalid_page(self):
        factories.CompanyFactory.build_batch(5)
        url = reverse('contacts_company_list_paginated', kwargs={'page': 3})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)


class CompanyDetailsTest(TestCase):
    def test_view(self):
        company = factories.CompanyFactory()
        url = reverse('contacts_company_detail', kwargs={'pk': company.id})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_unfound(self):
        url = reverse('contacts_company_detail', kwargs={'pk': 42})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 404)


class CompanyCreateTest(TestCase):
    url = reverse('contacts_company_create')

    def setUp(self):
        self.user = factories.UserFactory(is_staff=False, is_superuser=False)
        self.admin = factories.UserFactory()

    def test_get(self):
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 200)

    def test_create(self):
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(self.url, {
            'name': 'Foo',
            'nickname': 'foo',
            'about': 'bar',
        })
        self.failUnlessEqual(response.status_code, 302)

    def test_unvalid_form(self):
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(self.url, {'foo': 'bar'})
        self.failUnlessEqual(response.status_code, 500)

    def test_forbidden(self):
        self.client.login(username=self.user.username, password='foo')
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 403)
        response = self.client.post(self.url)
        self.failUnlessEqual(response.status_code, 403)


class CompanyUpdateTest(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(is_staff=False, is_superuser=False)
        self.admin = factories.UserFactory()
        self.company = factories.CompanyFactory()

    def test_get(self):
        url = reverse('contacts_company_update', kwargs={'pk': self.company.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_post(self):
        url = reverse('contacts_company_update', kwargs={'pk': self.company.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, COMPANY_UPDATE_POST)
        self.failUnlessEqual(response.status_code, 302)

    def test_post_unvalid_form(self):
        url = reverse('contacts_company_update', kwargs={'pk': self.company.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {})
        self.failUnlessEqual(response.status_code, 200)

    def test_unfound(self):
        url = reverse('contacts_company_update', kwargs={'pk': 42})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 404)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 404)

    def test_forbidden(self):
        url = reverse('contacts_company_update', kwargs={'pk': self.company.pk})
        self.client.login(username=self.user.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 403)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 403)


class CompanyDeleteTest(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(is_staff=False, is_superuser=False)
        self.admin = factories.UserFactory()
        self.company = factories.CompanyFactory()

    def test_get(self):
        url = reverse('contacts_company_delete', kwargs={'pk': self.company.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_post(self):
        url = reverse('contacts_company_delete', kwargs={'pk': self.company.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {'delete_company': 'Yes'})
        self.failUnlessEqual(response.status_code, 302)
        self.assertFalse(models.Company.objects.exists())

    def test_post_unconfirmed(self):
        url = reverse('contacts_company_delete', kwargs={'pk': self.company.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {'delete_company': ''})
        self.failUnlessEqual(response.status_code, 302)
        self.assertTrue(models.Company.objects.exists())

    def test_unfound(self):
        url = reverse('contacts_company_delete', kwargs={'pk': 42})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 404)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 404)

    def test_forbidden(self):
        url = reverse('contacts_company_delete', kwargs={'pk': self.company.pk})
        self.client.login(username=self.user.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 403)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 403)


class PersonListTest(TestCase):
    url = reverse('contacts_person_list')

    def test_view(self):
        factories.PersonFactory.build_batch(25)
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 200)

    def test_empty(self):
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 200)

    def test_paginated(self):
        factories.PersonFactory.build_batch(25)
        url = reverse('contacts_person_list_paginated', kwargs={'page': 1})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_no_previous_and_no_next(self):
        factories.PersonFactory.build_batch(5)
        url = reverse('contacts_person_list_paginated', kwargs={'page': 1})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_invalid_page(self):
        factories.PersonFactory.build_batch(5)
        url = reverse('contacts_person_list_paginated', kwargs={'page': 3})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)


class PersonDetailsTest(TestCase):
    def test_view(self):
        person = factories.PersonFactory()
        url = reverse('contacts_person_detail', kwargs={'pk': person.id})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_unfound(self):
        url = reverse('contacts_person_detail', kwargs={'pk': 42})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 404)


class PersonCreateTest(TestCase):
    url = reverse('contacts_person_create')

    def setUp(self):
        self.user = factories.UserFactory(is_staff=False, is_superuser=False)
        self.admin = factories.UserFactory()

    def test_get(self):
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 200)

    def test_create(self):
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(self.url, {
            'first_name': 'Foo',
            'last_name': 'Bar',
        })
        self.failUnlessEqual(response.status_code, 302)

    def test_unvalid_form(self):
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(self.url, {'foo': 'bar'})
        self.failUnlessEqual(response.status_code, 200)

    def test_forbidden(self):
        self.client.login(username=self.user.username, password='foo')
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 403)
        response = self.client.post(self.url)
        self.failUnlessEqual(response.status_code, 403)


class PersonUpdateTest(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(is_staff=False, is_superuser=False)
        self.admin = factories.UserFactory()
        self.person = factories.PersonFactory()

    def test_get(self):
        url = reverse('contacts_person_update', kwargs={'pk': self.person.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_post(self):
        url = reverse('contacts_person_update', kwargs={'pk': self.person.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, PERSON_UPDATE_POST)
        self.failUnlessEqual(response.status_code, 302)

    def test_post_unvalid_form(self):
        url = reverse('contacts_person_update', kwargs={'pk': self.person.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {})
        self.failUnlessEqual(response.status_code, 500)

    def test_unfound(self):
        url = reverse('contacts_person_update', kwargs={'pk': 42})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 404)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 404)

    def test_forbidden(self):
        url = reverse('contacts_person_update', kwargs={'pk': self.person.pk})
        self.client.login(username=self.user.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 403)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 403)


class PersonDeleteTest(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(is_staff=False, is_superuser=False)
        self.admin = factories.UserFactory()
        self.person = factories.PersonFactory()

    def test_get(self):
        url = reverse('contacts_person_delete', kwargs={'pk': self.person.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_post(self):
        url = reverse('contacts_person_delete', kwargs={'pk': self.person.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {'delete_person': 'Yes'})
        self.failUnlessEqual(response.status_code, 302)
        self.assertFalse(models.Person.objects.exists())

    def test_post_unconfirmed(self):
        url = reverse('contacts_person_delete', kwargs={'pk': self.person.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {'delete_person': ''})
        self.failUnlessEqual(response.status_code, 302)
        self.assertTrue(models.Person.objects.exists())

    def test_unfound(self):
        url = reverse('contacts_person_delete', kwargs={'pk': 42})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 404)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 404)

    def test_forbidden(self):
        url = reverse('contacts_person_delete', kwargs={'pk': self.person.pk})
        self.client.login(username=self.user.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 403)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 403)


class GroupListTest(TestCase):
    url = reverse('contacts_group_list')

    def test_view(self):
        factories.GroupFactory.build_batch(25)
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 200)

    def test_empty(self):
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 200)

    def test_paginated(self):
        factories.GroupFactory.build_batch(25)
        url = reverse('contacts_group_list_paginated', kwargs={'page': 1})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_no_previous_and_no_next(self):
        factories.GroupFactory.build_batch(5)
        url = reverse('contacts_group_list_paginated', kwargs={'page': 1})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_invalid_page(self):
        factories.GroupFactory.build_batch(5)
        url = reverse('contacts_group_list_paginated', kwargs={'page': 3})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)


class GroupDetailsTest(TestCase):
    def test_view(self):
        group = factories.GroupFactory()
        url = reverse('contacts_group_detail', kwargs={'pk': group.id})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_unfound(self):
        url = reverse('contacts_group_detail', kwargs={'pk': 42})
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 404)


class GroupCreateTest(TestCase):
    url = reverse('contacts_group_create')

    def setUp(self):
        self.user = factories.UserFactory(is_staff=False, is_superuser=False)
        self.admin = factories.UserFactory()

    def test_get(self):
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 200)

    def test_create(self):
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(self.url, {
            'name': 'Foo',
        })
        self.failUnlessEqual(response.status_code, 302)

    def test_unvalid_form(self):
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(self.url, {'foo': 'bar'})
        self.failUnlessEqual(response.status_code, 500)

    def test_forbidden(self):
        self.client.login(username=self.user.username, password='foo')
        response = self.client.get(self.url)
        self.failUnlessEqual(response.status_code, 403)
        response = self.client.post(self.url)
        self.failUnlessEqual(response.status_code, 403)


class GroupUpdateTest(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(is_staff=False, is_superuser=False)
        self.admin = factories.UserFactory()
        self.group = factories.GroupFactory()

    def test_get(self):
        url = reverse('contacts_group_update', kwargs={'pk': self.group.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_post(self):
        url = reverse('contacts_group_update', kwargs={'pk': self.group.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {'about': '', 'name': 'GroupA'})
        self.failUnlessEqual(response.status_code, 302)

    def test_post_unvalid_form(self):
        url = reverse('contacts_group_update', kwargs={'pk': self.group.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {})
        self.failUnlessEqual(response.status_code, 200)

    def test_unfound(self):
        url = reverse('contacts_group_update', kwargs={'pk': 42})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 404)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 404)

    def test_forbidden(self):
        url = reverse('contacts_group_update', kwargs={'pk': self.group.pk})
        self.client.login(username=self.user.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 403)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 403)


class GroupDeleteTest(TestCase):
    def setUp(self):
        self.user = factories.UserFactory(is_staff=False, is_superuser=False)
        self.admin = factories.UserFactory()
        self.group = factories.GroupFactory()

    def test_get(self):
        url = reverse('contacts_group_delete', kwargs={'pk': self.group.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)

    def test_post(self):
        url = reverse('contacts_group_delete', kwargs={'pk': self.group.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {'delete_group': 'Yes'})
        self.failUnlessEqual(response.status_code, 302)
        self.assertFalse(models.Group.objects.exists())

    def test_post_unconfirmed(self):
        url = reverse('contacts_group_delete', kwargs={'pk': self.group.pk})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.post(url, {'delete_group': ''})
        self.failUnlessEqual(response.status_code, 302)
        self.assertTrue(models.Group.objects.exists())

    def test_unfound(self):
        url = reverse('contacts_group_delete', kwargs={'pk': 42})
        self.client.login(username=self.admin.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 404)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 404)

    def test_forbidden(self):
        url = reverse('contacts_group_delete', kwargs={'pk': self.group.pk})
        self.client.login(username=self.user.username, password='foo')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 403)
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 403)
