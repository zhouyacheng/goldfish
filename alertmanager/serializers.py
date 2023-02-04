from rest_framework import serializers
from common.serializer import (
    AuthorSummaryModelSerializer,
    MutationSerializerMixin,
    CreationSerializerMixin,
    BaseModelSerializer,
    DateTimeModelSerializer,
)
from .models import AlertManager


class AlertManagerModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = AlertManager
        fields = ["id","receiver","job","fingerprint","status","alertname",
                  "instance","description","summary",
                  "severity","groupkey","start_time","end_time"]

class AlertManagerCreationModelSerializer(
    CreationSerializerMixin,
    AlertManagerModelSerializer,
):
    class Meta:
        model = AlertManager
        fields = ["receiver","job","fingerprint","status","alertname",
                  "instance","description","summary",
                  "severity","groupkey","start_time","end_time"]


class AlertManagerMutationModelSerializer(
    MutationSerializerMixin,
    AlertManagerModelSerializer,
):
    class Meta:
        model = AlertManager
        fields = ["id","receiver","job","fingerprint","status","alertname",
                  "instance","description","summary",
                  "severity","groupkey","start_time","end_time"]
