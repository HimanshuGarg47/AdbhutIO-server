from django.urls import path

from chat import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:project_id>/', consumers.ChatConsumer.as_asgi()),
]
