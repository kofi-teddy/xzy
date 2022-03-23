from rest_framework import serializers

from incidents.models import Incident, Site, Update, Uptime


class SiteSerializer(serializers.ModelSerilizer):
    class Meta:
        model = Site
        fields = ('id', 'title', 'url', 'date')


class UpdateSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Update
        fields = ('id', 'description', 'status', 'date')