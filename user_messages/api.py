from django.contrib.auth import SESSION_KEY
from django.contrib.messages import api, constants
from django.db import models
from django.utils import timezone
from django.utils.functional import SimpleLazyObject


def add_message(user, level, message, extra_tags='', *,
                deliver_once=True, meta=None):
    from user_messages.models import Message

    Message.objects.create(
        message={
            'level': level,
            'message': str(message),
            'extra_tags': extra_tags,
        },
        deliver_once=deliver_once,
        meta=meta or {},
        **{'user' if isinstance(user, models.Model) else 'user_id': user}
    )


def get_messages(*, request=None, user=None):
    assert bool(request) != bool(user), 'Pass exactly one of request or user'

    def fetch():
        nonlocal user

        messages = []

        if request is not None:
            messages.extend(api.get_messages(request))
            if (request.session.get(SESSION_KEY) and
                    request.user.is_authenticated):
                user = request.user

        if user is not None:
            from user_messages.models import Message

            m = Message.objects.filter(
                user=user,
                delivered_at__isnull=True,
            )
            messages.extend(m)
            m.filter(
                deliver_once=True,
            ).update(
                delivered_at=timezone.now(),
            )

        return messages

    return SimpleLazyObject(fetch)


def _create_shortcut(level):
    def helper(user, message, extra_tags='', deliver_once=True, meta=None):
        add_message(user, level, message, extra_tags=extra_tags,
                    deliver_once=deliver_once, meta=meta)
    return helper


debug = _create_shortcut(constants.DEBUG)
info = _create_shortcut(constants.INFO)
success = _create_shortcut(constants.SUCCESS)
warning = _create_shortcut(constants.WARNING)
error = _create_shortcut(constants.ERROR)
