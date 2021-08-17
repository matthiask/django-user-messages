==========
Change log
==========

`Next version`_
===============

- Switched to a declarative setup.
- Switched from Travis CI to GitHub actions.


`0.7`_ (2020-01-22)
===================

- Fixed a crash because of unicode strings being returned from
  ``Message.__str__`` in Python 2.
- Order messages upon retrieval.
- Added Django 3.0 to the Travis CI matrix.
- Replaced ``ugettext*`` with ``gettext*`` to avoid deprecation
  warnings.


`0.6`_ (2018-09-26)
===================

- Reformatted the code using black.
- Added a hint about silencing the messages context processor system
  check under Django 2.2.


`0.5`_ (2018-03-04)
===================

- Added german translations and a nice app name.
- Changed the implementation of keyword-only arguments to be compatible
  with Python 2.


`0.4`_ (2017-07-19)
===================

- **Backwards incompatible** Rebuilt the model to not use Django's
  ``JSONField`` at all. This design decision unnecessarily restricted
  the areas where django-user-messages was usable.
- Fixed properties to be more forgiving with missing data.
- Added tox configuration for running tests and coding style checks and for
  building the docs.
- Improved documentation and test coverage.


`0.3`_ (2017-05-18)
===================

- Added usage instructions.
- Merge the ``message`` and ``meta`` JSON fields into a single ``data``
  field and imitate the ``Message`` object interface more closely.


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
.. _0.3: https://github.com/matthiask/django-user-messages/compare/0.2...0.3
.. _0.4: https://github.com/matthiask/django-user-messages/compare/0.3...0.4
.. _0.5: https://github.com/matthiask/django-user-messages/compare/0.4...0.5
.. _0.6: https://github.com/matthiask/django-user-messages/compare/0.5...0.6
.. _0.7: https://github.com/matthiask/django-user-messages/compare/0.6...0.7
.. _Next version: https://github.com/matthiask/django-user-messages/compare/0.7...master
