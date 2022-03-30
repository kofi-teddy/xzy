from django.shortcuts import render

from rest_framework import permissions, mixins, viewsets

from apps.incidents.serializers import SubscriberSerializer


class SubscriberView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny)
    serializer_class = SubscriberSerializer