================================================================
django-user-messages - Offline addon for django.contrib.messages
================================================================

django-user-messages adds offline messaging support to Django's
messaging framework. It achieves this by allowing to save messages in
the database. The ``user_messages.api.get_messages`` utility and the
``user_messages.context_processors.messages`` context processor
transparently concatenate Django's messages and our own messages in a single
list, therefore existing code works without any changes and without
causing database writes.  django-user-messages' functions have to be
used explicitly. I consider this a feature, not a bug.


Installation
============

- Install ``django-user-messages`` using pip into your virtualenv.
- Replace ``django.contrib.messages`` with ``user_messages`` in 
  ``INSTALLED_APPS``
- Replace the default messages context processor with
  ``user_messages.context_processors.messages``. The context processor
  provides both django.contrib.messages' and django-user-messages'
  messages. 
- Add ``"admin.E404"`` and ``"admin.E406"`` to the 
  ``SILENCED_SYSTEM_CHECKS`` setting. This is because Django's admin 
  app checks for the presence of the default messages context processor 
  (admin.E404) and the default messages app in INSTALLED_APPS (E406), 
  so you'll have to silence these checks.
- Run ``./manage.py migrate``
- Use ``user_messages.api`` as you would use
  ``django.contrib.messages`` except that you pass the user model or ID
  as first parameter, not the current request.


Usage
=====

Pretty much the same as Django's messaging framework::

    from user_messages import api

    api.info(user, 'Hey there')
    api.warning(user, 'Stop this')
    api.error(user, 'Not nice!')

    # Passing the ID is also possible; the user instance does not
    # have to be instantiated at all:
    api.success(user.id, 'Yay!')

django-user-messages' messages supports two additional features not
available in Django's messages framework:

- Messages can be delivered more than once by passing
  ``deliver_once=False``. These messages have to be acknowledged
  explicitly. django-user-messages does not contain any code to do this.
- It is possible to attach additional data by passing a dictionary as
  ``meta``::

    api.debug(user, 'Oww', meta={
        'url': 'http://example.com',
    })

For convenience, our messages have the same ``tags`` and ``level_tag``
properties as Django's messages. Meta properties are also accessible in
templates::

    {% if messages %}
      <ul class="messages">
      {% for message in messages %}
        <li class="{{ message.tags }}".>
          {% if message.meta.url %}<a href="{{ message.meta.url }}">{% endif %}
          {{ message }}
          {% if message.meta.url %}</a>{% endif %}
        </li>
      {% endfor %}
      </ul>
    {% endif %}

django-user-messages' messages are also evaluated lazily.
