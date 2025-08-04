
# This configuration file is for Gunicorn, a Python WSGI HTTP Server for UNIX.
# It is used to serve your Django application in production.
# The settings below are optimized for a typical Django application.
bind = "0.0.0.0:8000"
workers = 3
worker_class = "gevent"
timeout = 120
loglevel = "info"
accesslog = "-"
errorlog = "-"