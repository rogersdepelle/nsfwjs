#!/bin/sh

python manage.py migrate --fake-initial

if [ "$MODE" = "development" ]; then
  python manage.py createsuperuser --noinput
fi

exec "$@"
