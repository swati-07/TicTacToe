"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from Home.consumers import GameRoom
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

ws_pattern=[
	path('ws/game/<room_code>',GameRoom.as_asgi())
]
application= ProtocolTypeRouter(
	{
	'websocket':AuthMiddlewareStack(URLRouter(
		ws_pattern
		))
	})