from django import VERSION
from django.apps import AppConfig
from django.conf import settings
from django.core import checks
from django.template import engines
from django.template.backends.django import DjangoTemplates
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _


@checks.register()
def check_context_processors(app_configs, **kwargs):
    errors = []

    if VERSION < (2, 2):
        # The admin.E404 check has been introduced in the Django 2.2 cycle.
        return errors

    for engine in engines.all():
        if isinstance(engine, DjangoTemplates):
            django_templates_instance = engine.engine
            break
    else:
        django_templates_instance = None

    if django_templates_instance:
        if (
            "django.contrib.messages.context_processors.messages"
            not in django_templates_instance.context_processors
            and "admin.E404" not in settings.SILENCED_SYSTEM_CHECKS
        ):
            errors.append(
                checks.Error(
                    "If using 'user_messages.context_processors.messages'"
                    " instead of the official messages context processor"
                    " you have to add 'admin.E404' to SILENCED_SYSTEM_CHECKS.",
                    id="user_messages.E001",
                )
            )

    if ("admin.E406" not in settings.SILENCED_SYSTEM_CHECKS and
    "django.contrib.messages" not in settings.INSTALLED_APPS):
        errors.append(
            checks.Error(
                "If using 'user_messages' instead of django.contrib.messages"
                " you have to add 'admin.E406' to SILENCED_SYSTEM_CHECKS.",
                id="user_messages.E002",
            )
        )

    return errors


class UserMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "user_messages"
    verbose_name = capfirst(_("user messages"))
