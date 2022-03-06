from channels.generic.websocket import AsyncWebSocketConsumer


class UpdateConsumer(AsyncWebSocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'All',
            self.channel_name
        )
        await self.accept()