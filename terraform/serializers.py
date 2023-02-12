from rest_framework import serializers
from common.serializer import (
    AuthorSummaryModelSerializer,
    MutationSerializerMixin,
    CreationSerializerMixin,
    BaseModelSerializer,
    DateTimeModelSerializer,
)
from .models import Terraform,TerraformPlan,TerraformTask

class TerraformModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = Terraform
        fields = "__all__"


class TerraformSummaryModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = Terraform
        fields = ["pk","name","tf",]


class TerraformCreationModelSerializer(
    CreationSerializerMixin,
    TerraformModelSerializer,
):
    class Meta:
        model = Terraform
        fields = "__all__"


class TerraformMutationModelSerializer(
    MutationSerializerMixin,
    TerraformModelSerializer,
):
    class Meta:
        model = Terraform
        fields = "__all__"


class TerraformPlanModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    terraform = TerraformSummaryModelSerializer(read_only=True)

    class Meta:
        model = TerraformPlan
        fields = "__all__"


class TerraformPlanSummaryModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = TerraformPlan
        fields = ["error_code","error_message","result"]

class TerraformPlanCreationModelSerializer(
    CreationSerializerMixin,
    TerraformPlanModelSerializer,
):
    terraform = serializers.PrimaryKeyRelatedField(queryset=Terraform.objects.all())

    class Meta:
        model = TerraformPlan
        fields = "__all__"


class TerraformPlanMutationModelSerializer(
    MutationSerializerMixin,
    TerraformPlanModelSerializer,
):
    terraform = serializers.PrimaryKeyRelatedField(queryset=Terraform.objects.all())

    class Meta:
        model = TerraformPlan
        fields = "__all__"


class TerraformTaskModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    terraform = TerraformSummaryModelSerializer(read_only=True)

    class Meta:
        model = TerraformTask
        fields = "__all__"


class TerraformTaskSummaryModelSerializer(
    AuthorSummaryModelSerializer,
    DateTimeModelSerializer,
    BaseModelSerializer,
    serializers.ModelSerializer,
):
    class Meta:
        model = TerraformTask
        fields = ["error_code","error_message","result"]

class TerraformTaskCreationModelSerializer(
    CreationSerializerMixin,
    TerraformTaskModelSerializer,
):
    terraform = serializers.PrimaryKeyRelatedField(queryset=Terraform.objects.all())

    class Meta:
        model = TerraformTask
        fields = "__all__"


class TerraformTaskMutationModelSerializer(
    MutationSerializerMixin,
    TerraformTaskModelSerializer,
):
    terraform = serializers.PrimaryKeyRelatedField(queryset=Terraform.objects.all())

    class Meta:
        model = TerraformTask
        fields = "__all__"