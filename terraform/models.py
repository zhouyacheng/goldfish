from django.db import models
from django.contrib.auth.models import User
from common.models import AuthorModel, BaseModel, DatetimeModel
from alertmanager.models import Project


class TerraformExecuteBase(
    AuthorModel,
    BaseModel,
    DatetimeModel,
    models.Model,
):
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, db_column="project_id"
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column="user_id")
    error_code = models.IntegerField(null=True)
    error_message = models.TextField(null=True)
    result = models.TextField(null=True)


class Terraform(
    AuthorModel,
    BaseModel,
    DatetimeModel,
    models.Model,
):
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, db_column="project_id"
    )
    name = models.CharField(max_length=64)
    tf = models.TextField(null=True)
    store = models.FileField(upload_to="tf_repository",verbose_name="上传目录")
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_column="user_id")

    class Meta:
        db_table = "terraform"


class TerraformPlan(TerraformExecuteBase):
    terraform = models.ForeignKey(Terraform,on_delete=models.PROTECT,db_column="terraform_id")

    class Meta:
        db_table = "terraform_plan"


class TerraformTask(TerraformExecuteBase):
    terraform = models.ForeignKey(Terraform, on_delete=models.PROTECT, db_column="terraform_id")

    class Meta:
        db_table = "terraform_task"
