"""
WSGI config for Scoopy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Scoopy.settings')

# application = get_wsgi_application()


import os
import sys

# Add your project directory to the sys.path
project_home = '/home/jiten08/Scoopy'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable to tell Django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'Scoopy.settings'

# Serve Django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
