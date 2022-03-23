from rest_framework import serializers

from incidents.models import Incident, Site, Update, Uptime


class SiteSerializer(serializers.ModelSerilizer):
    class Meta:
        model = Site
        fields = ('id', 'title', 'url', 'date')