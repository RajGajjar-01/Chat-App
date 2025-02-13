from channels.generic.websocket import AsyncWebsocketConsumer
import json
from . import models
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        self.user = self.scope["user"]

        # Reject the connection if the user is not authenticated
        if not self.user.is_authenticated:
            await self.close()
            return

        self.room = await self.get_room(self.room_name)

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.save_message(self.user, self.room, message)
        # Send the message back to the sender (self) with sender="self"
        await self.send(text_data=json.dumps({
            "message": message,
            "sender": "self", 
            "username": self.user.username, # Indicate that this message is sent by the current user
        }))

        # Broadcast the message to the room group, excluding self
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": "other",  # Indicate that this message is received from another user
                "username": self.user.username,  # Include the sender's username
                "sender_channel_name": self.channel_name,
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket, but exclude the sender
        message = event["message"]
        sender = event["sender"]
        username = event["username"]
        sender_channel_name = event["sender_channel_name"]

        # Only send the message if it's not from this connection
        if self.channel_name != sender_channel_name:
            await self.send(text_data=json.dumps({
                "message": message,
                "sender": sender,  # Include sender information
                "username": username,  # Include the sender's username
            }))

    @sync_to_async
    def get_room(self, room_name):
        # Fetch the Room object from the database
        return models.Room.objects.get(name=room_name)

    @sync_to_async
    def save_message(self, user, room, message):
        # Save the message to the database
        models.Message.objects.create(room=room, sender=user, message=message)