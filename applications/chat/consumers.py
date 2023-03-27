import json
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room, Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)


        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )


    async def chat_message(self, event):
        message = event['message']
        username = event['username']


        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message)
# class ChatNotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         user = self.scope['user']
#         if user.is_anonymous:
#             await self.close()
#         else:
#             await self.channel_layer.group_add(
#                 f"user_{user.id}",
#                 self.channel_name
#             )
#             await self.accept()
#
#     async def disconnect(self, close_code):
#         user = self.scope['user']
#         if not user.is_anonymous:
#             await self.channel_layer.group_discard(
#                 f"user_{user.id}",
#                 self.channel_name
#             )
#
#     async def chat_notification(self, event):
#         message = event['message']
#         chat_id = event['chat_id']
#         await self.send(text_data=json.dumps({
#             'type': 'chat_notification',
#             'message': message,
#             'chat_id': chat_id
#         }))
#
#
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         user = self.scope['user']
#         if user.is_anonymous:
#             await self.close()
#         else:
#             await self.channel_layer.group_add(
#                 f"user_{user.id}",
#                 self.channel_name
#             )
#             await self.accept()
#
#     async def disconnect(self, close_code):
#         user = self.scope['user']
#         if not user.is_anonymous:
#             await self.channel_layer.group_discard(
#                 f"user_{user.id}",
#                 self.channel_name
#             )
#
#     async def chat_message(self, event):
#         message = event['message']
#         chat_id = event['chat_id']
#         await self.send(text_data=json.dumps({
#             'type': 'chat_message',
#             'message': message,
#             'chat_id': chat_id
#         }))