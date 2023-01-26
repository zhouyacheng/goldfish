from rest_framework import serializers
from .models import Task, TaskState, Repository, Template, Release, TaskEvent, Stats, PeriodTask
from common.serializer import DateTimeModelSerializer, BaseModelSerializer, FormDataFileField,MutationSerializerMixin,AuthorSummaryModelSerializer
from django_celery_beat.models import PeriodicTask,CrontabSchedule,IntervalSchedule
from timezone_field.rest_framework import TimeZoneSerializerField

class RepositorySummaryModelSerializer(MutationSerializerMixin,BaseModelSerializer,DateTimeModelSerializer,serializers.ModelSerializer):
    display_name = serializers.CharField(read_only=True)
    class Meta:
        model = Repository
        fields = ["id","name","display_name"]

class RepositoryModelSerializer(MutationSerializerMixin,BaseModelSerializer,DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):
    # store = FormDataFileField()
    display_name = serializers.CharField(read_only=True)
    webhook_url = serializers.CharField(read_only=True)


    class Meta:
        model = Repository
        fields = [
            "id","is_deleted","orders","create_time","update_time","url","owner",
            "delete_time","name","created_by","updated_by","deleted_by","display_name","token","provider_class",
            "webhook_url"
        ]
        extra_kwargs = {
            "signature":{"read_only": True},
        }


class ReleaseModelSummarySerializer(BaseModelSerializer,DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):
    repository = RepositorySummaryModelSerializer()
    owner = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    version_name = serializers.CharField(read_only=True)

    class Meta:
        model = Release
        fields = "__all__"

class IntervalScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = "__all__"

class CrontabScheduleSerializer(serializers.ModelSerializer):
    timezone = TimeZoneSerializerField()
    class Meta:
        model = CrontabSchedule
        fields = "__all__"

class PeriodicTaskModelSerializer(DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = "__all__"

class PeriodTaskModelSerializer(BaseModelSerializer,DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):
    interval = IntervalScheduleSerializer(required=False)
    crontab = CrontabScheduleSerializer(required=False)
    release = ReleaseModelSummarySerializer()

    class Meta:
        model = PeriodTask
        exclude = ["beat"]


class PeriodTaskCreationModelSerializer(PeriodTaskModelSerializer):
    release = serializers.PrimaryKeyRelatedField(queryset=Release.objects.all())

    class Meta:
        model = PeriodTask
        exclude = ["beat"]

    def validate(self, attrs :dict):
        scheduler_types = ["interval","crontab"]
        selected_scheduler_types = [i for i in scheduler_types if attrs.get(i)]
        if len(selected_scheduler_types) != 1:
            raise serializers.ValidationError("Only one of interval or crontab must be set.")
        return attrs

    def create(self, validated_data :dict):
        interval = validated_data.pop("interval",None)
        if interval:
            validated_data["interval"] = IntervalSchedule.objects.create(**interval)
        crontab = validated_data.pop("crontab", None)
        if crontab:
            validated_data["crontab"] = CrontabSchedule.objects.create(**crontab)
        return PeriodTask.objects.create(**validated_data)


class PeriodTaskSummaryModelSerializer(PeriodTaskModelSerializer):
    crontab = serializers.StringRelatedField(read_only=True)
    interval = serializers.StringRelatedField(read_only=True)
    release = ReleaseModelSummarySerializer()
    class Meta:
        model = PeriodTask
        exclude = ["beat"]

class PeriodTaskMutationSerializer(MutationSerializerMixin,PeriodTaskModelSerializer):
    release = serializers.PrimaryKeyRelatedField(queryset=Release.objects.all())

    class Meta:
        model = PeriodTask
        exclude = ["beat"]

    def validate(self, attrs :dict):
        scheduler_types = ["interval","crontab"]
        selected_scheduler_types = [i for i in scheduler_types if attrs.get(i)]
        if len(selected_scheduler_types) > 1:
            raise serializers.ValidationError("Only one of interval or crontab must be set.")
        return attrs

    @classmethod
    def _update_child(cls, model, data :dict,model_id):
        if not data:
            return
        else:
            # pk = data.pop("id", None)
            instance = model.objects.filter(pk=model_id).first()
            print(instance)
            if not instance:
                return
            for k, v in data.items():
                setattr(instance, k, v)
            instance.save()
            return instance

    def update(self, instance :PeriodicTask, validated_data :dict):
        interval_id = instance.interval_id
        if interval_id:
            interval = self._update_child(IntervalSchedule, validated_data.pop("interval", None),interval_id)
            instance.interval = interval
            instance.crontab = None

        crontab_id = instance.crontab_id
        if crontab_id:
            crontab = self._update_child(CrontabSchedule, validated_data.pop("crontab",None),crontab_id)
            instance.interval = None
            instance.crontab = crontab
        for k,v in validated_data.items():
            setattr(instance,k,v)
        instance.save()
        return instance
class StatsModelSerializer(DateTimeModelSerializer,serializers.ModelSerializer):

    class Meta:
        model = Stats
        fields = "__all__"
class TaskModelSerializer(BaseModelSerializer,DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):
    # state = serializers.ChoiceField(choices=TaskState.choices,default=TaskState.PENDING,read_only=True)
    class Meta:
        model = Task
        fields = ["id","create_time","update_time","delete_time","release","playbook",
            "role","envvars","extravars","forks","timeout","state","output","created_by",
                  "updated_by","deleted_by","inventories"
        ]
        extra_kwargs = {
            "output": {"read_only": True},
            "state": {"read_only": True},
        }


class TaskModelSummarySerializer(BaseModelSerializer,DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):
    # state = serializers.ChoiceField(choices=TaskState.choices,default=TaskState.PENDING,read_only=True)
    # repository = RepositorySummaryModelSerializer(read_only=True)
    release = ReleaseModelSummarySerializer()
    #
    tasks = StatsModelSerializer(many=True,read_only=True)
    period = PeriodTaskSummaryModelSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ["id","create_time","update_time","delete_time","release","playbook",
                  "role","envvars","extravars","forks","timeout","state","output","created_by",
                  "updated_by","deleted_by","inventories","tasks","period"
        ]
        extra_kwargs = {
            "output": {"read_only": True},
            "state": {"read_only": True},
        }


class TemplateModelSerializer(BaseModelSerializer,DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):
    # repository = RepositorySummaryModelSerializer()
    release = ReleaseModelSummarySerializer()

    class Meta:
        model = Template
        fields = "__all__"

class TemplateCreationModelSerializer(BaseModelSerializer,DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):
    # repository = serializers.PrimaryKeyRelatedField(queryset=Repository.objects.filter(is_deleted=0))
    release = serializers.PrimaryKeyRelatedField(queryset=Release.objects.filter(is_deleted=0))

    class Meta:
        model = Template
        fields = "__all__"

class TemplateMutationSerializer(MutationSerializerMixin,TemplateModelSerializer):
    release = serializers.PrimaryKeyRelatedField(queryset=Release.objects.filter(is_deleted=0))

    class Meta:
        model = Template
        fields = "__all__"

class ReleaseModelSerializer(BaseModelSerializer,DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    version_name = serializers.CharField(read_only=True)
    class Meta:
        model = Release
        fields = "__all__"


class TaskEventModelSerializer(BaseModelSerializer,DateTimeModelSerializer,AuthorSummaryModelSerializer,serializers.ModelSerializer):

    class Meta:
        model = TaskEvent
        fields = "__all__"





