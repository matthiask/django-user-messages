================================================================
django-user-messages - Offline addon for django.contrib.messages
================================================================

.. image:: https://travis-ci.org/matthiask/django-user-messages.svg?branch=master
   :target: https://travis-ci.org/matthiask/django-user-messages


Usage
=====

- Install ``django-user-messages`` using pip into your virtualenv.
- Add ``user_messages`` to ``INSTALLED_APPS`` and run ``migrate``.
- Replace the default messages context processor with
  ``user_messages.context_processors.messages``. The context processor
  provides both django.contrib.messages' and django-user-messages'
  messages.
- Use ``user_messages.api`` as you would use
  ``django.contrib.messages``.
