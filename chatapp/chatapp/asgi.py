"""
ASGI config for chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

# application = get_asgi_application()
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
        'websocket':AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
        )
    # Use channels for handling WebSockets
    # Add other protocols as needed
})
