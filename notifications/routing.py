from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from notifications import consumer



websocket_patterns=[
    re_path(r'ws/notification/$',consumer.NotificationConsumer.as_asgi())
]
# application = ProtocolTypeRouter({
#     "websocket": URLRouter([
#         re_path(r"^/ws/notifications", consumer.NotificationConsumer)
#
#     ]),
# })
