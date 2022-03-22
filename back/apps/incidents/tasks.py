from celery import shared_task
import requests
from datetime import datetime 
from request.exceptions import ConnectionError, Timeout
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from incidents.models import Site, Uptime



sites = Site.objects.all()
for site in sites:
    try:
        r = requests.head(site.url, timeout=4)
        Uptime.objects.create(
            site=site, status='up',
            response_time=int(r.elapsed.total_seconds() * 1000),
            date=datetime.now()
            )
    except Timeout as e:
        Uptime.objects.create(
            site=site, 
            status='up',
            response_time=4000,
            date=datetime.now())
    except Exception as e:
        Uptime.objects.create(
            site=site, 
            status='down', 
            response_time=0, 
            date=datetime.now()
            )

channel_layer = get_channel_layer()
async_to_sync(channel_layer.group_send)(
    'All', {'type': 'chat_message', 'message': data}
)


@shared_task
def update_to_visitor():
    print('Task update_to_visitor has been initiated')


