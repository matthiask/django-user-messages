from django.apps import AppConfig
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


class UserMessagesConfig(AppConfig):
    name = 'user_messages'
    verbose_name = capfirst(_('user messages'))
