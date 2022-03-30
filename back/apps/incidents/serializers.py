from rest_framework import serializers

from apps.incidents.models import Incident, Site, Update, Uptime, Subscriber

class UpdateSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Update
        fields = ('id', 'description', 'status', 'date')

class UptimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Uptime
        fields = ('id', 'date', 'response_time', 'status')


class IncidentSerializer(serializers.ModelSerializer):
    update_set = UpdateSerializer(many=True, read_only=True)

    class Meta:
        model = Incident
        fields = ('id', 'title', 'update_set', 'start', 'end', 'solved')


class SiteSerializer(serializers.ModelSerializer):
    uptime_set = UptimeSerializer(many=True, read_only=True, source='last_30_uptime_items')
    incident_set = IncidentSerializer(many=True, read_only=True, source='last_7_days_incident_items')
    
    class Meta:
        model = Site
        fields = ('id', 'title', 'url', 'date')


class SubscriberSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        if Subscriber.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError('subscriber with this email already exists.')
        return value.lower()

    class Meta:
        model = Subscriber
        fields = ('email',)