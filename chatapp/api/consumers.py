# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GrpMsgConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Add the user to the "chat_group" group
        await self.channel_layer.group_add(
            "chat_group",
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the "chat_group" group
        await self.channel_layer.group_discard(
            "chat_group",
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Broadcast the message to all users in the group
        await self.channel_layer.group_send(
            "chat_group",
            {
                "type": "chat.message",
                "message": message,
            },
        )

    async def chat_message(self, event):
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
