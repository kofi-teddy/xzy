from rest_framework import serializers

from incidents.models import Incident, Site, Update, Uptime


class UpdateSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Update
        fields = ('id', 'description', 'status', 'date')

class UptimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Update
        fields = ('id', 'date', 'response_time', 'status')


class IncidentSerializer(serializers.ModelSerializer):
    update_set = UpdateSerializer(many=True, read_only=True)

    class Meta:
        model = Incident
        fields = ('id', 'title', 'update_set', 'start', 'end', 'solved')


class SiteSerializer(serializers.ModelSerilizer):
    uptime_set = UptimeSerializer(many=True, read_only=True, source='last_30_uptime_items')
    incident_set = IncidentSerializer(many=True, read_only=True, source='last_7_days_incident_items')
    
    class Meta:
        model = Site
        fields = ('id', 'title', 'url', 'date')