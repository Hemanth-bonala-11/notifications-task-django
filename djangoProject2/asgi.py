"""
ASGI config for djangoProject2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django

from django.core.asgi import get_asgi_application





from channels.routing import ProtocolTypeRouter, URLRouter
from notifications import consumer

from notifications.routing import websocket_patterns
from channels.auth import AuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject2.settings')
django.setup()

application = ProtocolTypeRouter({
    "http":get_asgi_application(),

    "websocket":
        URLRouter(
            websocket_patterns
        )

})

