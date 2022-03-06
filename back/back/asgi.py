"""
ASGI config for back project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from incidents import routing
from django.core.asgi import get_wsgi_application


application = ProtocolTypeRouter({
    'http': get_wsgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})
