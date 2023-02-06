from rest_framework import serializers
from common.serializer import (
    AuthorSummaryModelSerializer,
    MutationSerializerMixin,
    CreationSerializerMixin,
    BaseModelSerializer,
    DateTimeModelSerializer,
)
from .models import AlertManager,Project,AppAlertmanagerUserResult,AppAlertmanagerJobResult,AppAlertmanagerJobStatusResult

class ProjectModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = Project
        fields = ["name","role","user"]


class ProjectSummaryModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = Project
        fields = ["name","role","user"]

class ProjectCreationModelSerializer(
    CreationSerializerMixin,
    ProjectModelSerializer,
):
    class Meta:
        model = Project
        fields = ["name","role","user"]


class ProjectMutationModelSerializer(
    MutationSerializerMixin,
    ProjectModelSerializer,
):
    class Meta:
        model = Project
        fields = ["name","role","user"]



class AlertManagerModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = AlertManager
        fields = ["id","project","receiver","job","fingerprint","status","alertname",
                  "instance","description","summary",
                  "severity","groupkey","start_time","end_time"]

class AlertManagerCreationModelSerializer(
    CreationSerializerMixin,
    AlertManagerModelSerializer,
):
    class Meta:
        model = AlertManager
        fields = ["project","receiver","job","fingerprint","status","alertname",
                  "instance","description","summary",
                  "severity","groupkey","start_time","end_time"]


class AlertManagerMutationModelSerializer(
    MutationSerializerMixin,
    AlertManagerModelSerializer,
):
    class Meta:
        model = AlertManager
        fields = ["id","project","receiver","job","fingerprint","status","alertname",
                  "instance","description","summary",
                  "severity","groupkey","start_time","end_time"]


class AppAlertmanagerUserResultModelSerializer(serializers.ModelSerializer,):
    class Meta:
        model = AppAlertmanagerUserResult
        fields = "__all__"


class AppAlertmanagerJobResultModelSerializer(serializers.ModelSerializer,):
    class Meta:
        model = AppAlertmanagerJobResult
        fields = "__all__"

class AppAlertmanagerJobStatusResultModelSerializer(serializers.ModelSerializer,):
    class Meta:
        model = AppAlertmanagerJobStatusResult
        fields = "__all__"
