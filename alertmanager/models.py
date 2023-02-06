from django.db import models
from django.contrib.auth.models import User
from common.models import AuthorModel,BaseModel,DatetimeModel


class Project(AuthorModel,BaseModel,DatetimeModel,models.Model,):
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=64,null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column="user_id")

class AlertManager(AuthorModel,BaseModel,DatetimeModel,models.Model,):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, db_column="project_id")
    receiver = models.CharField(max_length=64)
    job = models.CharField(max_length=64)
    fingerprint = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    alertname = models.CharField(max_length=64)
    instance = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    summary = models.CharField(max_length=256)
    severity = models.CharField(max_length=64)
    groupkey = models.CharField(max_length=512)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
