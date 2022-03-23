from django.contrib import admin

from apps.incidents.models import Site, Uptime, Incident, Update


admin.site.register(Site)
admin.site.register(Uptime)
admin.site.register(Incident)
admin.site.register(Update)