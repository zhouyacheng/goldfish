import yaml
import json
import logging
from django.core.exceptions import ValidationError
from django.db import models
from urllib.parse import urlparse
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.utils.module_loading import import_string
from packaging.version import Version
from common.models import BaseModel, DatetimeModel, AuthorModel
from .repositories import BaseRepositoryProvider
from django_celery_beat.models import IntervalSchedule,PeriodicTask,CrontabSchedule
from channels.layers import get_channel_layer,InMemoryChannelLayer
from asgiref.sync import async_to_sync
# import hashlib


def clean_provider_class(value):
    try:
        if value:
            clazz = import_string(value)
            if issubclass(clazz, BaseRepositoryProvider):
                return value
    except (ValidationError,ImportError):
        raise ValidationError("Invaild provider class.")
    except Exception:
        pass


class Repository(BaseModel, DatetimeModel, AuthorModel, models.Model):
    owner = models.CharField(max_length=50, verbose_name="仓库属主")
    name = models.CharField(max_length=50, verbose_name="仓库名称")
    # store = models.FileField(upload_to="repository",verbose_name="上传目录")
    # signature = models.CharField(max_length=40,verbose_name="签名")
    url = models.URLField(verbose_name="gitea url")
    token = models.CharField(max_length=40, default="", verbose_name="gitea token")
    provider_class = models.CharField(max_length=128,validators=[clean_provider_class],default="iac.repositories.GiteaRepositoryProvider",verbose_name="指定git仓库使用对应的provider来获取仓库信息")

    @cached_property
    def provider(self):
        clazz = import_string(self.provider_class)
        if issubclass(clazz,BaseRepositoryProvider):
            return clazz(url=self.url,token=self.token)

    @property
    def webhook_url(self):
        return reverse_lazy("repository-webhook",kwargs={"pk": self.id})
    @property
    def display_name(self):
        url = urlparse(self.url)
        _, owner, name = url.path.split("/")
        self.owner = owner
        self.name = name
        return f"{self.owner}/{self.name}"

    # @property
    # def extract(self):
    #     return (str(self.store).split("/")[0],str(self.store).split("/")[1])
    #
    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     with self.store.open("rb") as f:
    #         hasher = hashlib.sha1()
    #         if f.multiple_chunks():
    #             for chunk in f.chunks():
    #                 hasher.update(chunk)
    #         else:
    #             hasher.update(f.read())
    #         self.signature = hasher.hexdigest()
    #         super().save(force_insert,force_update,using,update_fields)

    class Meta:
        db_table = "repository"
        unique_together = ["owner", "name", "is_deleted"]


class TaskState(models.IntegerChoices):
    PENDING = 0, "PENDING"
    RUNNING = 1, "RUNNING"
    COMPLETED = 2, "COMPLETED"
    FAILED = 3, "FAILED"
    CANCELED = 4, "CANCELED"
    TIMEOUT = 5, "TIMEOUT"
    UNKNOW = 6, "UNKNOW"


class BaseTask(BaseModel, DatetimeModel, AuthorModel, models.Model):
    release = models.ForeignKey(
        "Release", on_delete=models.RESTRICT, db_column="release_id"
    )
    playbook = models.CharField(
        max_length=50, default="main.yaml", verbose_name="playbook目录"
    )
    role = models.CharField(max_length=50, null=True, default="", verbose_name="role")
    inventories = models.TextField(null=True, blank=True, verbose_name="主机清单")
    envvars = models.TextField(null=True, default="", verbose_name="环境变量")
    extravars = models.TextField(null=True, default="", verbose_name="额外变量")
    forks = models.IntegerField(default=1, verbose_name="线程数")
    timeout = models.IntegerField(default=3600, verbose_name="超时时间(秒)")

    class Meta:
        abstract = True


class Task(BaseTask):
    state = models.IntegerField(choices=TaskState.choices, default=TaskState.PENDING)
    output = models.TextField(null=True, default="")
    period = models.ForeignKey("PeriodTask",on_delete=models.PROTECT,db_column="period_id",related_name="periods",null=True)


    class Meta:
        db_table = "task"

    def __str__(self):
        return f"<TASK: {self.release.repository.name}/{self.playbook}>"

    def _load(self, data):
        result = ""
        if data:
            try:
                result = json.loads(data)
            except ValueError:
                pass
            except Exception as e:
                print(e)

            try:
                result = yaml.safe_load(data)
            except yaml.YAMLError:
                pass
        return result

    def to_runner_kwargs(self):
        envvars = self._load(self.envvars)
        extravars = self._load(self.extravars)
        role = self.role
        inventories = self.inventories
        kwarg = {
            "playbook": self.playbook,
            "forks": self.forks,
            "timeout": self.timeout,
        }
        if envvars:
            kwarg["envvars"] = envvars
        if extravars:
            kwarg["extravars"] = extravars
        if role:
            kwarg["role"] = role
        if inventories:
            kwarg["inventory"] = inventories
        return kwarg

    @classmethod
    def get_channel_group_name(cls, task_id):
        return f"iac_task_{task_id}"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(Task,self).save(force_insert,force_update,using,update_fields)
        self.handle_task_changed()


    @async_to_sync
    async def handle_task_changed(self):
        channel_layer :InMemoryChannelLayer = get_channel_layer()
        channel_group = self.get_channel_group_name(self.pk)
        await channel_layer.group_send(channel_group,{"type":"on_task_changed","data": self.pk})


class Template(BaseTask):
    name = models.CharField(max_length=128, unique=True, verbose_name="模板名称")
    description = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="描述"
    )

    class Meta:
        db_table = "template"


class Release(BaseModel, DatetimeModel, AuthorModel, models.Model):
    repository = models.ForeignKey(
        Repository,
        on_delete=models.PROTECT,
        db_column="repository_id",
        verbose_name="仓库",
        related_name="releases",
    )
    archive_url = models.URLField(verbose_name="playbook目录")
    major = models.IntegerField(verbose_name="主版本")
    minor = models.IntegerField(verbose_name="次版本")
    micro = models.IntegerField(verbose_name="小版本")
    commit = models.CharField(max_length=40, default="", verbose_name="提交id")
    @property
    def version(self):
        return Version(f"{self.major}.{self.minor}.{self.micro}")

    @property
    def version_name(self):
        return self.version

    class Meta:
        db_table = "release"
        ordering = ["-major", "-minor", "-micro"]
        unique_together = ["repository_id", "major", "minor", "micro"]


class MissionState(models.IntegerChoices):
    OK = 0,"ok"
    FAILED = 1,"failed"
    SKIPPED = 2,"skipped"
    UNREACHABLE = 3,"unreachable"
class TaskEvent(DatetimeModel,models.Model):

    task = models.ForeignKey(Task,on_delete=models.PROTECT,db_column="task_id",related_name="events")
    state = models.IntegerField(choices=MissionState.choices)
    play = models.CharField(max_length=512)
    mission = models.CharField(max_length=512)
    host = models.CharField(max_length=512)
    ip = models.CharField(max_length=512)
    start = models.DateTimeField()
    end = models.DateTimeField()
    duration = models.FloatField()
    changed = models.BooleanField()
    detail = models.JSONField()
    play_pattern = models.CharField(max_length=128)
    counter = models.IntegerField()

    class Meta:
        db_table = "taskevent"


class Stats(DatetimeModel,models.Model):
    task = models.ForeignKey(Task,on_delete=models.PROTECT,db_column="task_id",related_name="tasks")
    host = models.CharField(max_length=128)
    ip = models.CharField(max_length=128)
    ok = models.IntegerField(default=0)
    dark = models.IntegerField(default=0)
    failures = models.IntegerField(default=0)
    changed = models.IntegerField(default=0)
    ignored = models.IntegerField(default=0)
    processed = models.IntegerField(default=0)
    rescued = models.IntegerField(default=0)
    skipped = models.IntegerField(default=0)
    artifact_data = models.CharField(max_length=1024,blank=True,null=True)


class PeriodTask(BaseTask):
    name = models.CharField(max_length=200)
    interval = models.ForeignKey(IntervalSchedule,on_delete=models.CASCADE,null=True)
    crontab = models.ForeignKey(CrontabSchedule,on_delete=models.CASCADE,null=True)
    enabled = models.BooleanField(default=True)
    beat = models.ForeignKey(PeriodicTask,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = "periodtask"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(PeriodTask,self).save(force_insert,force_update,using,update_fields)
        print(f"self.beat: {self.beat}")
        if self.beat:
            self.beat.interval = self.interval
            self.beat.crontab = self.crontab
            self.beat.enabled = self.enabled
            self.beat.args = json.dumps([self.pk])
            self.beat.save()
        else:
            self.beat = PeriodicTask.objects.create(
                name=self.name,
                task="iac.tasks.execute_period_task",
                interval=self.interval,
                crontab=self.crontab,
                enabled=self.enabled,
                args=json.dumps([self.pk]),
            )
            self.save_base()
