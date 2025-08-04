"""
WSGI config for hello_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/

to be called in the terminal from `app` directory with:
`gunicorn core.wsgi:application`
"""

import os
from core.settings import DJANGO_ENV

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"core.settings.{DJANGO_ENV}")
print(f"WSGI application loaded in {DJANGO_ENV} mode.")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()