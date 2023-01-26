from rest_framework import serializers
from common.serializer import (
    AuthorSummaryModelSerializer,
    MutationSerializerMixin,
    CreationSerializerMixin,
    BaseModelSerializer,
    DateTimeModelSerializer,
)
from .models import (
    Project,
    ProjectEnv,
    Stage,
    StageType,
    ProjectResource,
    ReleaseTask,
    ReleaseTaskHistory,
    Pipeline,
    ReleaseTaskProgress,
)
from rest_framework.serializers import PrimaryKeyRelatedField

class StageOrderSerializer(serializers.Serializer):
    stages = serializers.ListSerializer(child=serializers.IntegerField())

class PipelineModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = Pipeline
        fields = "__all__"


class PipelineSummaryModelSerializer(PipelineModelSerializer):
    class Meta:
        model = Pipeline
        fields = ["id", "name"]


class PipelineCreationModelSerializer(CreationSerializerMixin, PipelineModelSerializer):
    class Meta:
        model = Pipeline
        fields = "__all__"


class PipelineMutationModelSerializer(MutationSerializerMixin, PipelineModelSerializer):
    class Meta:
        model = Pipeline
        fields = "__all__"


class ProjectModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    pipeline = PipelineSummaryModelSerializer(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectSummaryModelSerializer(
    ProjectModelSerializer, serializers.ModelSerializer
):
    pipeline = PipelineSummaryModelSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name"]


class ProjectCreationModelSerializer(
    CreationSerializerMixin, ProjectModelSerializer, serializers.ModelSerializer
):
    pipeline = PrimaryKeyRelatedField(queryset=Pipeline.objects.all())

    class Meta:
        model = Project
        fields = "__all__"


class ProjectMutationModelSerializer(
    MutationSerializerMixin, ProjectModelSerializer, serializers.ModelSerializer
):
    pipeline = PrimaryKeyRelatedField(queryset=Pipeline.objects.all())

    class Meta:
        model = Project
        fields = "__all__"


class StageModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    pipeline = PipelineSummaryModelSerializer(read_only=True)

    class Meta:
        model = Stage
        fields = "__all__"


class StageSummaryModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    pipeline = PipelineSummaryModelSerializer(read_only=True)

    class Meta:
        model = Stage
        fields = ["id", "name", "stage_type", "seq", "pipeline"]


class StageCreationModelSerializer(CreationSerializerMixin, StageModelSerializer):
    pipeline = PrimaryKeyRelatedField(queryset=Pipeline.objects.all())

    class Meta:
        model = Stage
        exclude = ["seq"]


class StageMutationModelSerializer(MutationSerializerMixin, StageModelSerializer):
    pipeline = PrimaryKeyRelatedField(queryset=Pipeline.objects.all())

    class Meta:
        model = Stage
        exclude = ["seq"]


class ProjectEnvModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    project = ProjectSummaryModelSerializer()
    # stage = StageSummaryModelSerializer()
    stage = StageModelSerializer()

    class Meta:
        model = ProjectEnv
        fields = "__all__"


# class ProjectEnvModelSummarySerializer(ProjectModelSerializer,serializers.ModelSerializer):
#     class Meta:
#         model = ProjectEnv
#         fields = ["id","name","value"]


class ProjectEnvCreationModelSerializer(
    CreationSerializerMixin, ProjectModelSerializer, serializers.ModelSerializer
):
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())
    stage = PrimaryKeyRelatedField(queryset=Stage.objects.all())

    class Meta:
        model = ProjectEnv
        fields = "__all__"


class ProjectEnvMutationModelSerializer(
    MutationSerializerMixin, ProjectModelSerializer, serializers.ModelSerializer
):
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())
    stage = PrimaryKeyRelatedField(queryset=Stage.objects.all())

    def create(self, validated_data):
        pk = validated_data.get("pk", None)
        name = validated_data.get("name", None)
        value = validated_data.get("value", None)
        print(pk, name, value)
        return ProjectEnv.objects.create(**validated_data)

    def update(self, instance, validated_data):
        method = validated_data.pop("method", None)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save(method=method)
        return instance

    class Meta:
        model = ProjectEnv
        fields = "__all__"


class ProjectResourceModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    project = ProjectSummaryModelSerializer()
    # stage = StageSummaryModelSerializer()
    stage = StageModelSerializer()

    class Meta:
        model = ProjectResource
        fields = "__all__"


# class ProjectResourceModelSummarySerializer(ProjectModelSerializer,serializers.ModelSerializer):
#     class Meta:
#         model = ProjectResource
#         fields = ["id","name","value"]


class ProjectResourceCreationModelSerializer(
    CreationSerializerMixin, ProjectModelSerializer, serializers.ModelSerializer
):
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())
    stage = PrimaryKeyRelatedField(queryset=Stage.objects.all())

    class Meta:
        model = ProjectResource
        fields = "__all__"


class ProjectResourceMutationModelSerializer(
    MutationSerializerMixin, ProjectModelSerializer, serializers.ModelSerializer
):
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())
    stage = PrimaryKeyRelatedField(queryset=Stage.objects.all())

    class Meta:
        model = ProjectResource
        fields = "__all__"


class ReleaseTaskModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    project = ProjectSummaryModelSerializer()
    # current = StageSummaryModelSerializer()
    current = StageModelSerializer()

    class Meta:
        model = ReleaseTask
        fields = "__all__"


class ReleaseTaskCreationModelSerializer(
    CreationSerializerMixin,
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())
    # current = PrimaryKeyRelatedField(queryset=Stage.objects.all())

    class Meta:
        model = ReleaseTask
        # fields = "__all__"
        exclude = ["current"]


class ReleaseTaskMutationModelSerializer(
    MutationSerializerMixin, ReleaseTaskModelSerializer
):
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())
    current = PrimaryKeyRelatedField(queryset=Stage.objects.all())

    class Meta:
        model = ReleaseTask
        fields = "__all__"


class ReleaseTaskHistoryModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = ReleaseTaskHistory
        fields = "__all__"


class ReleaseTaskProgressModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = ReleaseTaskProgress
        fields = "__all__"
