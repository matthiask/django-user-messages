from django.contrib.auth import SESSION_KEY
from django.contrib.messages import add_message
from django.utils import timezone

from .api import get_messages


def user_messages_middleware(get_response):
    def middleware(request):
        if request.session.get(SESSION_KEY) and request.user.is_authenticated:
            messages = get_messages(request.user)
            once = False
            for message in messages:
                add_message(request, **message.message)
                once = once or message.deliver_once
            if once:
                messages.filter(
                    deliver_once=True,
                ).update(
                    delivered_at=timezone.now(),
                )
        return get_response(request)
    return middleware
