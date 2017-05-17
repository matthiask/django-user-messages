from django.contrib.messages import constants

from user_messages.models import Message


def add_message(user, level, message, extra_tags='', *, deliver_once=True):
    Message.objects.create(
        user=user,
        message={
            'level': level,
            'message': str(message),
            'extra_tags': extra_tags,
        },
        deliver_once=deliver_once,
    )


def get_messages(user):
    return Message.objects.filter(
        user=user,
        delivered_at__isnull=True,
    )


def _create_shortcut(level):
    def helper(user, message, extra_tags='', deliver_once=True):
        add_message(user, level, message, extra_tags=extra_tags,
                    deliver_once=deliver_once)
    return helper


debug = _create_shortcut(constants.DEBUG)
info = _create_shortcut(constants.INFO)
success = _create_shortcut(constants.SUCCESS)
warning = _create_shortcut(constants.WARNING)
error = _create_shortcut(constants.ERROR)
