from django.urls import path
from .consumers import GrpMsgConsumer

websocket_urlpatterns = [
    path('ws/grpmsg/', GrpMsgConsumer.as_asgi()),
]