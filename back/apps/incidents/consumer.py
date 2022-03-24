import json

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebSocketConsumer

from apps.incidents.models import Site
from apps.incidents.serializers import SiteSerializer


class UpdateConsumer(AsyncWebSocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'All',
            self.channel_name
        )
        await self.accept()
        await self.send_sites()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'All',
            self.channel_name
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def send_sites(self):
        sites = sites.objects.all()
        for site in sites:
            serializer = SiteSerializer(site)
            async_to_sync(self.chat_message)(
                {'type': 'chat_message', 'message': serializer.data }
            )
        
    

