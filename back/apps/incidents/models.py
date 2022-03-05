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


class Incident(models.Model):
    '''
    An Incident is an event that is an inconvenience, be it downtime or maintenance.
    An Incident is linked to Update, as an Incident should contain multiple Updates 
    to keep the users up to date on the latest progress. An Incident should also be linked to a Site, since we could have multiple sites to watch and we want to know which site has an issue.
    '''
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start = models.DateTimeField(auto_now_add=True)
    end = models.BooleanField(default=False)
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




