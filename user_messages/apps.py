from django.apps import AppConfig
from django.core import checks
from django.template import engines
from django.template.backends.django import DjangoTemplates
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _


@checks.register()
def check_context_processors(app_configs, **kwargs):
    errors = []

    for engine in engines.all():
        if isinstance(engine, DjangoTemplates):
            context_processors = engine.engine.context_processors
            try:
                dj = context_processors.index(
                    "django.contrib.messages.context_processors.messages"
                )
                um = context_processors.index(
                    "user_messages.context_processors.messages"
                )
            except ValueError:
                continue
            if um < dj:
                errors.append(
                    checks.Error(
                        "Insert 'user_messages.context_processors.messages' after 'django.contrib.messages.context_processors.messages' so that the 'messages' context variable actually contains user messages.",
                        id="user_messages.E002",
                    )
                )

    return errors


class UserMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "user_messages"
    verbose_name = capfirst(_("user messages"))
