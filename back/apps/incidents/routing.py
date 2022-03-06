from django.urls import path


websocket_urlpatterns = [
    path('ws/', apps.incidents.consumer.UpdateConsumer.as_asgi())
]