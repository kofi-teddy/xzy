from django.shortcuts import render

from rest_framework import permissions, mixins, viewsets
from rest_framework import Response

from incidents.serializers import SubscriberSerializer


class SubscriberView(mixins.CreateModelMixin, viewsets.GenericViewset):
    permission_classes = (permissions.AllowAny)
    serializer_class = SubscriberSerializer