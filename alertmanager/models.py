from django.db import models
from common.models import AuthorModel,BaseModel,DatetimeModel


class AlertManager(AuthorModel,BaseModel,DatetimeModel,models.Model,):
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