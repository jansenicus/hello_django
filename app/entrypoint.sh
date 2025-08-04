#!/bin/sh

echo "Cleaning __pycache__ and .pyc files..."
find . -type d -name "__pycache__" -exec rm -r {} + -print
find . -type f -name "*.pyc" -exec rm {} + -print

if [ "$DJANGO_ENV" = "development" ]; then
  echo "Running migrations for dev..."
  python manage.py flush --no-input
  python manage.py migrate
else
  echo "Skipping flush in production."
fi

exec "$@"