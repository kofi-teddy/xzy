from django.db import models


class Incident(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start = models.DateTimeField(auto_now_add=True)
    end = models.BooleanField(default=False)

    def __str__(self):
        return self.title


