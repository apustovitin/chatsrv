from django.urls import path, re_path
from public_chat.consumers import PublicChatConsumer

websocket_urlpatterns = [
    re_path(r'public_chat/(?P<room_id>\w+)/$', PublicChatConsumer.as_asgi()),
]
