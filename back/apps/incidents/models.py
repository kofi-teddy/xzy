from django.conf import settings
from django.db import models


class Site(models.Model):
    '''
    At last, a Site should also be linked to multiple Uptime events.
    We want to know every minute if our site is up or not, and we will store that with Uptime records.
    '''
    title = models.CharField(max_length=255)
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def last_30_uptime_items(self):
        return self.uptime_set.all().order_by('-date')[:30]


class Incident(models.Model):
    '''
    An Incident is an event that is an inconvenience, be it downtime or maintenance.
    An Incident is linked to Update, as an Incident should contain multiple Updates 
    to keep the users up to date on the latest progress. An Incident should also be linked to a Site, since we could have multiple sites to watch and we want to know which site has an issue.
    '''
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


UPTIME_STATUS_CHOICES = (
    ('up', 'All is good'),
    ('issue', 'We are having some issues'),
    ('down', 'Our website is down'),
)


class Uptime(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    response_time = models.IntegerField() 
    status = models.CharField(max_length=10, choices=UPTIME_STATUS_CHOICES)

    def __str__(self):
        return str(self.response_time)


UPDATE_STATUS_CHOICES = (
    ('identified', 'Identified'),
    ('investigating', 'Investigating'),
    ('monitoring', 'Monitoring'),
    ('resolved', 'Resolved')
)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, default=None)
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, null=True, default=None)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=UPDATE_STATUS_CHOICES)

    def __str__(self):
        return f'{self.incident.title} - {self.description:20}'


