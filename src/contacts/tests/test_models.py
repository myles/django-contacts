from django.test import TestCase
from contacts.tests import factories


class CompanyTest(TestCase):
    def setUp(self):
        self.company = factories.CompanyFactory(name='Foo')

    def test_str(self):
        self.assertEqual(str(self.company), 'Foo')

    def test_get_absolute_url(self):
        self.assertEqual(self.company.get_absolute_url(), '/companies/1-foo/')

    def test_get_update_url(self):
        self.assertEqual(self.company.get_update_url(), '/companies/1-foo/edit/')

    def test_get_delete_url(self):
        self.assertEqual(self.company.get_delete_url(), '/companies/1-foo/delete/')

    def test_get_email(self):
        self.email = factories.EmailAddressFactory(content_object=self.company)
        email = self.company.email_address.get()
        self.failUnlessEqual(email.email_address, self.email.email_address)


class PersonTest(TestCase):
    def setUp(self):
        self.person = factories.PersonFactory()
        self.fullname = "%s %s" % (self.person.first_name, self.person.last_name)

    def test_str(self):
        self.assertEqual(self.fullname, str(self.person))

    def test_fullname(self):
        self.assertEqual(self.fullname, self.person.fullname)

    def test_get_absolute_url(self):
        url = '/people/%s-%s/' % (self.person.id, self.person.slug)
        self.assertEqual(self.person.get_absolute_url(), url)

    def test_get_update_url(self):
        url = '/people/%s-%s/edit/' % (self.person.id, self.person.slug)
        self.assertEqual(self.person.get_update_url(), url)

    def test_get_delete_url(self):
        url = '/people/%s-%s/delete/' % (self.person.id, self.person.slug)
        self.assertEqual(self.person.get_delete_url(), url)


class GroupTest(TestCase):
    def setUp(self):
        self.group = factories.GroupFactory()

    def test_str(self):
        self.assertEqual(self.group.name, str(self.group))

    def test_get_absolute_url(self):
        url = '/groups/%s-%s/' % (self.group.id, self.group.slug)
        self.assertEqual(self.group.get_absolute_url(), url)

    def test_get_update_url(self):
        url = '/groups/%s-%s/edit/' % (self.group.id, self.group.slug)
        self.assertEqual(self.group.get_update_url(), url)

    def test_get_delete_url(self):
        url = '/groups/%s-%s/delete/' % (self.group.id, self.group.slug)
        self.assertEqual(self.group.get_delete_url(), url)


class LocationTest(TestCase):
    def setUp(self):
        self.location = factories.LocationFactory()

    def test_str(self):
        self.assertEqual(self.location.name, str(self.location))


class PhoneNumberTest(TestCase):
    def setUp(self):
        self.number = factories.PhoneNumberFactory()

    def test_str(self):
        number_str = "%s (%s)" % (self.number.phone_number, self.number.location)
        self.assertEqual(number_str, str(self.number))


class EmailAddressTest(TestCase):
    def setUp(self):
        self.email = factories.EmailAddressFactory()

    def test_str(self):
        email_str = "%s (%s)" % (self.email.email_address, self.email.location)
        self.assertEqual(email_str, str(self.email))


class InstantMessengerTest(TestCase):
    def setUp(self):
        self.im = factories.InstantMessengerFactory()

    def test_str(self):
        im_str = "%s (%s)" % (self.im.im_account, self.im.location)
        self.assertEqual(im_str, str(self.im))


class WebSiteTest(TestCase):
    def setUp(self):
        self.website = factories.WebSiteFactory()

    def test_str(self):
        website_str = "%s (%s)" % (self.website.url, self.website.location)
        self.assertEqual(website_str, str(self.website))

    def test_get_absolute_url(self):
        url = '/people/%s-%s/?web_site=%s' % (self.website.content_object.id,
                                              self.website.content_object.slug,
                                              self.website.id)
        self.assertEqual(self.website.get_absolute_url(), url)


class StreetAddressTest(TestCase):
    def setUp(self):
        self.addr = factories.StreetAddressFactory()

    def test_str(self):
        addr_str = "%s (%s)" % (self.addr.city, self.addr.location)
        self.assertEqual(addr_str, str(self.addr))


class SpecialDateTest(TestCase):
    def setUp(self):
        self.date = factories.SpecialDateFactory()

    def test_str(self):
        date_str = "%s: %s" % (self.date.occasion, self.date.date)
        self.assertEqual(date_str, str(self.date))
