==========
Change log
==========

`Next version`_
===============

`0.2`_ (2017-05-18)
===================

- Added the possibility to associate additional data with a message py
  passing a dictionary as the ``meta`` keyword-only argument to the API.
- Changed the module to import the ``Message`` model as late as possible
  so that the API can easily be imported for example in a ``AppConfig``
  module.


`0.1`_ (2017-05-17)
===================

- Initial public release.

.. _django-user-messages: https://django-user-messages.readthedocs.io/

.. _0.1: https://github.com/matthiask/django-user-messages/commit/3a9c0e329e
.. _0.2: https://github.com/matthiask/django-user-messages/compare/0.1...0.2
.. _Next version: https://github.com/matthiask/django-user-messages/compare/0.2...master
