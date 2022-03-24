from datetime import datetime, timedelta

import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.conf import settings
from django.core.mail import EmailMessage
from request.exceptions import ConnectionError, Timeout
from users.models import User

from incidents.models import Site, Uptime
from incidents.serializers import SiteSerializer


@shared_task
def update_to_visitor():
    print('Task update_to_visitor has been initiated')
    sites = Site.objects.all()

    # ping all sites
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
    
    serializer = SiteSerializer(site)

    # send messages to groups
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'All', {'type': 'chat_message', 'message': serializer.data}
    )

    if not Uptime.objects.filter(status='issue', site=site, date__qte=datetime.now() - timedelta(minutes=10)).exist():
        emails = [x.email for x in User.objects.all() if x.email_for_issues]
        email = EmailMessage('We just had a time out', 'Please check our website, we might have issues. https://kofiteddy.com', 
            settings.DEFAULT_FROM_EMAIL, [User.objects.first().email], [emails], fail_silently=True)

        email.send()
