from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=0,verbose_name="逻辑删除")
    orders = models.IntegerField(verbose_name='显示顺序',default=0)

    class Meta:
        abstract = True

class DatetimeModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="修改时间")
    delete_time = models.DateTimeField(null=True,default=None,verbose_name="删除时间")

    class Meta:
        abstract = True

class AuthorModel(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True,verbose_name="创建者",related_name="+")
    updated_by = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True,verbose_name="修改者",related_name="+")
    deleted_by = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True,verbose_name="删除者",related_name="+")

    class Meta:
        abstract = True


class File(models.Model):
    uuid = models.UUIDField(max_length=512)
    name = models.CharField(max_length=61)
    size = models.BigIntegerField()
    path = models.CharField(max_length=128,null=True)


