"""
ASGI config for react_wagtail_app project.

It exposes the ASGI callable as a module-level variable named ``application``.
rrrrrrrr
For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'react_wagtail_app.settings')

application = get_asgi_application()
