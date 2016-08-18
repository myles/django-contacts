import os
from setuptools import setup, find_packages
import contacts


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-contacts',
    version=contacts.__version__,
    url=contacts.__url__,
    license=contacts.__license__,
    description=contacts.__doc__,
    long_description=read('README.rst'),

    author=contacts.__author__,
    author_email=contacts.__email__,

    packages=find_packages(),

    install_requires=read('requirements.txt').splitlines(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
