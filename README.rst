================================================================
django-user-messages - Offline addon for django.contrib.messages
================================================================

.. image:: https://travis-ci.org/matthiask/django-user-messages.svg?branch=master
   :target: https://travis-ci.org/matthiask/django-user-messages


Usage
=====

- Install ``django-user-messages`` using pip into your virtualenv.
- Add ``user_messages.middleware.user_messages_middleware`` to your
  ``MIDDLEWARE`` **after** ``MessagesMiddleware``.
- Add ``user_messages`` to ``INSTALLED_APPS`` and run ``migrate``.
- Use ``user_messages.api`` as you would use
  ``django.contrib.messages``.
