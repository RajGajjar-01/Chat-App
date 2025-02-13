# myproject/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chatApplication import routing

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    ),
})