import json
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from common.models import AuthorModel,BaseModel,DatetimeModel


class Pipeline(BaseModel,DatetimeModel,AuthorModel,models.Model):
    name = models.CharField(max_length=128)

class Project(AuthorModel,BaseModel,DatetimeModel,models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=256)
    build_template = models.TextField(blank=True)
    deploy_template = models.TextField()
    pipeline = models.ForeignKey(Pipeline,on_delete=models.PROTECT,db_column="pipeline_id")

    class Meta:
        unique_together = ["name","is_deleted"]


class StageType(models.IntegerChoices):
    BUILD = 0, "BUILD"
    DEPLOY = 1, "DEPLOY"


class BaseStage(models.Model):
    stage_type = models.IntegerField(choices=StageType.choices)
    name = models.CharField(max_length=64)
    seq = models.IntegerField()
    namespace = models.CharField(default='default', max_length=256)
    kubeconfig_content = models.TextField(null=True)
    context = models.TextField(null=True)

    class Meta:
        abstract = True

class Stage(BaseStage,BaseModel,DatetimeModel,AuthorModel):
    pipeline = models.ForeignKey(Pipeline, on_delete=models.PROTECT, db_column="pipeline_id")


class Env(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    value = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

class ProjectEnv(Env,BaseModel,DatetimeModel,AuthorModel):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,db_column="project_id")
    stage = models.ForeignKey(Stage,on_delete=models.CASCADE,db_column="stage_id")
    envs :dict = models.JSONField(null=True,blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None, method=None
    ):
        count = 0
        if method == "delete" or method == "update":
            super().save(force_insert=False, force_update=False, using=None, update_fields=None)
            return
        if self.envs:
            for name,value in self.envs.items():
                self.name = name
                self.value = value
                if count != 0:
                    self.pk = self.pk + 1
                if self.name != "env":
                    super().save(force_insert=False, force_update=False, using=None, update_fields=None)
                    count = 1
                else:
                    for item in self.envs[self.name]:
                        for child_name, child_value in item.items():
                            self.name = child_name
                            self.value = child_value
                            if count != 0:
                                self.pk = self.pk + 1
                            super().save(force_insert=False, force_update=False, using=None, update_fields=None)
                            count = 1


    class Meta:
        unique_together = ["project_id","stage_id","name"]

# class ContainerResourceType(models.IntegerChoices):
#     LIMITS = 0, "LIMITS"
#     REQUESTS = 1, "REQUESTS"
#
#
# class ContainerResource(DatetimeModel,models.Model):
#     limits_cpu = models.CharField(max_length=64)
#     limits_memory = models.CharField(max_length=64)
#     requests_cpu = models.CharField(max_length=64,null=True)
#     requests_memory = models.CharField(max_length=64,null=True)
#
#
# class ProjectDeploymentResource(DatetimeModel,models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE,db_column="project_id",related_name="projects")
#     stage = models.ForeignKey(Stage, on_delete=models.CASCADE,db_column="stage_id",related_name="stages")
#     container_resource = models.OneToOneField(ContainerResource,on_delete=models.PROTECT)
#     replicas = models.IntegerField(default=1)
#
#     class Meta:
#         unique_together = ["project_id","stage_id"]


class Resource(models.Model):
    limits_cpu = models.CharField(max_length=64)
    limits_memory = models.CharField(max_length=64)
    requests_cpu = models.CharField(max_length=64, null=True)
    requests_memory = models.CharField(max_length=64, null=True)
    replicas = models.IntegerField(default=1)
    backoff_limit = models.IntegerField(default=3)
    active_deadline_seconds = models.IntegerField(default=3600)

    class Meta:
        abstract = True

class ProjectResource(Resource,BaseModel,DatetimeModel,AuthorModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, db_column="project_id")
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, db_column="stage_id")
    containerPort = models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together = ["project_id","stage_id"]

class ReleaseTaskState(models.IntegerChoices):
    PENDING = 0, "PENDING"
    RUNNING = 1, "RUNNING"
    COMPLETED = 2, "COMPLETED"
    FAILED = 3, "FAILED"
    CLOSED = 4, "CLOSED"
    UNKONW = 5, "UNKONW"

class ReleaseTask(BaseModel,DatetimeModel,AuthorModel,models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, db_column="project_id")
    current = models.ForeignKey(Stage, on_delete=models.PROTECT, db_column="current_id")
    version = models.CharField(max_length=128)
    state = models.IntegerField(choices=ReleaseTaskState.choices,default=ReleaseTaskState.PENDING)
    render_template = models.TextField(null=True)
    observed_generation = models.BigIntegerField(null=True)

    class Meta:
        unique_together = ["project_id","version"]

class ReleaseTaskProgress(BaseStage,BaseModel,DatetimeModel,AuthorModel):
    task = models.ForeignKey(ReleaseTask, on_delete=models.PROTECT, db_column="task_id")
    state = models.IntegerField(choices=ReleaseTaskState.choices, default=ReleaseTaskState.PENDING)
    render_template = models.TextField(null=True)
    observed_generation = models.BigIntegerField(null=True)

class ReleaseTaskHistory(BaseModel,DatetimeModel,AuthorModel,models.Model):
    task = models.ForeignKey(ReleaseTask, on_delete=models.PROTECT, db_column="task_id")
    stage = models.ForeignKey(Stage, on_delete=models.PROTECT, db_column="stage_id")
    state = models.IntegerField(choices=ReleaseTaskState.choices,default=ReleaseTaskState.PENDING)
    render_template = models.TextField(null=True)
    observed_generation = models.BigIntegerField(null=True)


class EnvSnapshot(Env):
    stage = models.ForeignKey(ReleaseTaskProgress,on_delete=models.PROTECT,db_column="stage_id")


class ResourceSnapshot(Resource):
    stage = models.ForeignKey(ReleaseTaskProgress,on_delete=models.PROTECT,db_column="stage_id")


class Service(BaseModel,DatetimeModel,AuthorModel,models.Model):
    name = models.CharField(max_length=128,null=True)
    template = models.TextField()
    render_template = models.TextField(null=True)
    is_template = models.BooleanField(default=False)



class Configmap(BaseModel,DatetimeModel,AuthorModel,models.Model):
    name = models.CharField(max_length=128,null=True)
    template = models.TextField()
    render_template = models.TextField(null=True)
    is_template = models.BooleanField(default=False)


class CustomResourceDefinition(BaseModel,DatetimeModel,AuthorModel,models.Model):
    name = models.CharField(max_length=128)
    template = models.TextField()
    render_template = models.TextField(null=True)
    is_template = models.BooleanField(default=False)


class CustomResource(BaseModel,DatetimeModel,AuthorModel,models.Model):
    name = models.CharField(max_length=128)
    template = models.TextField()
    render_template = models.TextField(null=True)
    is_template = models.BooleanField(default=False)
    crd = models.ForeignKey(CustomResourceDefinition,on_delete=models.PROTECT,db_column="crd_id")