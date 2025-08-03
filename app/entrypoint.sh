#!/bin/sh

if [ "$DJANGO_ENV" = "development" ]; then
  echo "Running migrations for dev..."
  python manage.py flush --no-input
  python manage.py migrate
else
  echo "Skipping flush in production."
fi

exec "$@"