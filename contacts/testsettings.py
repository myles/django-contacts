DEBUG = True
DEBUG_TEMPLATE = True
SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/django-contacts-devel.db'
    }
}
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django_comments',
    'contacts',
]
ROOT_URLCONF = 'contacts.testurls'
SECRET_KEY = 'test-secret-key'
STATIC_URL = '/static/'
