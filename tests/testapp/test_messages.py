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
            '<ul class="messages"',
        )

        response = client.get('/')
        self.assertContains(
            response,
            '<ul class="messages" data-length="1">',
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

    def test_meta(self):
        user = User.objects.create_user(
            'test', 'test@example.com', 'test'
        )
        api.info(user, 'Hi', meta={
            'url': 'http://example.com',
        })

        m = api.get_messages(user=user)
        self.assertEqual(
            len(m),
            1,
        )
        self.assertEqual(
            m[0].data,
            {
                'message': 'Hi',
                'level': 20,
                'level_tag': 'info',
                'extra_tags': '',
                'meta': {
                    'url': 'http://example.com',
                },
            },
        )

        client = Client()
        client.force_login(user)
        api.info(user, 'Hey', meta={
            'url': 'http://example.com',
        })
        self.assertContains(
            client.get('/'),
            "<li class=\"info\">Hey http://example.com</li>",
        )
