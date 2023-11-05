import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "broadcast"
        self.room_group_name = 'notification_%s' % self.room_name


        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()



    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     print(message)
    #
    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )
    #     await  self.send("hrerkjlewnrkjewrn")

    async def receive(self, text_data):

        json_data=json.loads(text_data)
        print(type(json_data))

        num1=json_data["num1"]
        num2=json_data["num2"]
        print(num1,num2)
        print(type(int(num1)))
        print(type(int(num2)))

        # Send message to WebSocket
        response_data = {
             "result":int(num1) * int(num2)
        }
        await self.send(json.dumps(response_data))
    # Receive message from room group
    # async def send_notification(self, event):
    #     message = json.loads(event['message'])
    #
    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps(message))