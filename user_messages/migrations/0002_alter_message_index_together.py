# Generated by Django 4.0.2 on 2022-02-03 10:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_messages", "0001_initial"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="message",
            index_together={("user", "delivered_at")},
        ),
    ]
