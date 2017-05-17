from django.contrib.auth.models import User
from django.test import Client, TestCase

from user_messages import api


def _messages(response):
    return [m.message for m in response.context['messages']]


class MessagesTestCase(TestCase):
    def test_messages(self):
        user = User.objects.create_user(
            'test', 'test@example.com', 'test'
        )

        client = Client()
        client.force_login(user)

        api.error(user, 'Hello world')
        self.assertContains(
            client.get('/'),
            '<li class="error">Hello world</li>',
            1,
        )
        self.assertContains(
            client.get('/'),
            '<li class="error">Hello world</li>',
            0,
        )

        anonymous = Client()
        api.error(user, 'Hello world 2')

        self.assertNotContains(
            anonymous.get('/'),
            '<ul class="messages">',
        )

        response = client.get('/')
        self.assertContains(
            response,
            '<ul class="messages">',
        )
        self.assertContains(
            response,
            '<li class="error">Hello world 2</li>',
            1,
        )
        self.assertContains(
            client.get('/'),
            '<li class="error">Hello world 2</li>',
            0,
        )

    def test_deliver_multiple(self):
        user = User.objects.create_user(
            'test', 'test@example.com', 'test'
        )

        client = Client()
        client.force_login(user)

        api.error(user, 'Hello world', deliver_once=False)
        self.assertContains(
            client.get('/'),
            '<li class="error">Hello world</li>',
            1,
        )
        self.assertContains(
            client.get('/'),
            '<li class="error">Hello world</li>',
            1,
        )
