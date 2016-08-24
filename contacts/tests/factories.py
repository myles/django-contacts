import factory
from django.utils.text import slugify


class CompanyFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))

    class Meta:
        model = 'contacts.Company'


class PersonFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    slug = factory.LazyAttribute(lambda o: slugify(o.first_name[0].lower() + o.last_name))

    class Meta:
        model = 'contacts.Person'


class GroupFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))

    class Meta:
        model = 'contacts.Group'


class LocationFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))

    class Meta:
        model = 'contacts.Location'


class PhoneNumberFactory(factory.django.DjangoModelFactory):
    phone_number = factory.Faker('phone_number')

    object_id = factory.LazyAttribute(lambda o: o.content_object.id)
    content_object = factory.SubFactory(PersonFactory)

    location = factory.SubFactory(LocationFactory)

    class Meta:
        model = 'contacts.PhoneNumber'


class EmailAddressFactory(factory.django.DjangoModelFactory):
    email_address = factory.Faker('email')

    object_id = factory.LazyAttribute(lambda o: o.content_object.id)
    content_object = factory.SubFactory(PersonFactory)

    location = factory.SubFactory(LocationFactory)

    class Meta:
        model = 'contacts.EmailAddress'


class InstantMessengerFactory(factory.django.DjangoModelFactory):
    im_account = factory.Faker('user_name')

    object_id = factory.LazyAttribute(lambda o: o.content_object.id)
    content_object = factory.SubFactory(PersonFactory)

    location = factory.SubFactory(LocationFactory)

    class Meta:
        model = 'contacts.InstantMessenger'


class WebSiteFactory(factory.django.DjangoModelFactory):
    url = factory.Faker('url')

    object_id = factory.LazyAttribute(lambda o: o.content_object.id)
    content_object = factory.SubFactory(PersonFactory)

    location = factory.SubFactory(LocationFactory)

    class Meta:
        model = 'contacts.WebSite'


class StreetAddressFactory(factory.django.DjangoModelFactory):
    country = factory.Faker('country')
    city = factory.Faker('city')

    object_id = factory.LazyAttribute(lambda o: o.content_object.id)
    content_object = factory.SubFactory(PersonFactory)

    location = factory.SubFactory(LocationFactory)

    class Meta:
        model = 'contacts.StreetAddress'


class SpecialDateFactory(factory.django.DjangoModelFactory):
    occasion = factory.Faker('sentence')
    date = factory.Faker('date')

    object_id = factory.LazyAttribute(lambda o: o.content_object.id)
    content_object = factory.SubFactory(PersonFactory)

    class Meta:
        model = 'contacts.SpecialDate'


class UserFactory(factory.DjangoModelFactory):
    email = factory.Faker('email')
    username = factory.Faker('user_name')
    password = factory.PostGenerationMethodCall('set_password', 'foo')

    is_superuser = True
    is_staff = True
    is_active = True

    class Meta:
        model = 'auth.User'
