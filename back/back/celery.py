import os 
from celery import Celery
from django.conf import settings
import django
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')
django.setup()

# set the default Django settings module for the 'celery' program and scanning for tasks.
app = Celery('back')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)


app.conf.beat_schedule = {
    'every-minute-test-task': {
        'task': 'incidents.tasks.update_to_visitor',
        'schedule': crontab(minute='*')
    },
}