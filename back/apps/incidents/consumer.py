from channels.generic.websocket import AsyncWebSocketConsumer


class UpdateConsumer(AsyncWebSocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'All',
            self.channel_name
        )
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'All',
            self.channel_name
        )