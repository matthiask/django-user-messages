from django.contrib.auth.models import User
from django.test import Client, TestCase

from user_messages import api
from user_messages.models import Message


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

    def test_admin(self):
        user = User.objects.create_superuser(
            'test', 'test@example.com', 'test'
        )
        api.info(user, 'Hi', meta={
            'url': 'http://example.com',
        })
        m = list(api.get_messages(user=user))

        # Quite invalid. Still, shouldn't crash.
        Message.objects.create(
            user=user,
        )

        client = Client()
        client.force_login(user)

        self.assertEqual(
            client.get('/admin/user_messages/message/').status_code,
            200,
        )
        self.assertEqual(
            client.get(
                '/admin/user_messages/message/{}/change/'.format(m[0].id),
            ).status_code,
            200,
        )

    def test_both_frameworks(self):
        user = User.objects.create_user(
            'test', 'test@example.com', 'test'
        )
        client = Client()
        client.force_login(user)

        self.assertContains(
            client.get('/produce_message/'),
            'OK',
        )
        api.warning(
            user,
            'user_messages framework',
        )

        response = client.get('/')
        self.assertContains(
            response,
            '<ul class="messages" data-length="2">',
            1,
        )
        self.assertContains(
            response,
            '<li class="info">Default messages framework</li>',
            1,
        )
        self.assertContains(
            response,
            '<li class="warning">user_messages framework</li>',
            1,
        )
