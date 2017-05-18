from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    created_at = models.DateTimeField(
        _('created at'),
        default=timezone.now,
    )
    delivered_at = models.DateTimeField(
        _('delivered at'),
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('user'),
        related_name='+',
    )
    data = JSONField(
        _('data'),
        default=dict,
    )
    deliver_once = models.BooleanField(
        _('deliver once'),
        default=True,
    )

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')

    # Duck typing django.contrib.messages.storage.base.Message
    def __str__(self):
        return self.message

    @property
    def level(self):
        return self.data.get('level', 20)  # INFO

    @property
    def message(self):
        return self.data.get('message', '')

    @property
    def extra_tags(self):
        return self.data.get('extra_tags', '')

    @property
    def level_tag(self):
        return self.data.get('level_tag', 'info')

    @property
    def tags(self):
        return ' '.join(tag for tag in [
            self.extra_tags,
            self.level_tag,
        ] if tag)

    @property
    def meta(self):
        return self.data.get('meta', {})
