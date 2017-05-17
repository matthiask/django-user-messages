#!/bin/sh
venv/bin/coverage run --branch --include="*user_messages/*" --omit="*tests*,*migrations*" ./manage.py test -v 2 testapp
venv/bin/coverage html
