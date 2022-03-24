from django.urls import path

from apps.incidents import views


urlpatterns = [
    path('subscribe', views.SubscriberView),
]