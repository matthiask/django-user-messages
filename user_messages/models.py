import json

from django.conf import settings
from django.contrib.messages.storage.base import LEVEL_TAGS
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    created_at = models.DateTimeField(_("created at"), default=timezone.now)
    delivered_at = models.DateTimeField(_("delivered at"), blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="+",
    )
    level = models.IntegerField(_("level"))
    message = models.TextField(_("message"))
    extra_tags = models.TextField(_("extra tags"), blank=True)
    _metadata = models.TextField(_("meta data"), blank=True)
    deliver_once = models.BooleanField(_("deliver once"), default=True)

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")
        index_together = (("user", "delivered_at"),)

    def __str__(self):
        # Duck typing django.contrib.messages.storage.base.Message
        return self.message

    @property
    def level_tag(self):
        return LEVEL_TAGS.get(self.level, "")

    @property
    def tags(self):
        return " ".join(tag for tag in [self.extra_tags, self.level_tag] if tag)

    @cached_property
    def meta(self):
        if self._metadata:
            try:
                return json.loads(self._metadata)
            except Exception:
                pass
        return {}
