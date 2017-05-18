#!/usr/bin/env python3

import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='django-user-messages',
    version=__import__('user_messages').__version__,
    description='Offline addon for django.contrib.messages',
    long_description=read('README.rst'),
    author='Matthias Kestenholz',
    author_email='mk@feinheit.ch',
    url='http://github.com/matthiask/django-user-messages/',
    license='MIT License',
    platforms=['OS Independent'],
    packages=find_packages(
        exclude=['tests', 'testapp'],
    ),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
)
