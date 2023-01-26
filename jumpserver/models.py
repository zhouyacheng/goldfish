from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=255,null=True)
    level = models.IntegerField(default=1)
    parent = models.ForeignKey("self",models.PROTECT,null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "jmp_org"

    def __str__(self):
        return f"{self.pk} {self.name} {self.parent}"

class Host(models.Model):
    is_deleted_choice = (
        (0,"显示"),
        (1,"伪删除"),
    )

    name = models.CharField(max_length=255,null=False,blank=False,verbose_name="主机名称")
    alias_name = models.CharField(max_length=255,null=True,blank=True,verbose_name="主机别名")
    ip = models.GenericIPAddressField(verbose_name="ip地址")
    user = models.CharField(max_length=20,null=False,blank=False,verbose_name="主机登录用户",default="root")
    password = models.CharField(max_length=255,null=True,blank=True,verbose_name="主机密码")
    ssh_public_key_path = models.CharField(max_length=255,null=True,blank=False,verbose_name="公钥路径")
    ssh_private_key_path = models.CharField(max_length=255,null=True,blank=False,verbose_name="私钥路径")
    is_deleted = models.SmallIntegerField(default=0,verbose_name="伪删除",choices=is_deleted_choice)
    add_date = models.DateTimeField(auto_now_add=True)
    org = models.ForeignKey("Organization",on_delete=models.PROTECT,related_name="hosts")

    class Meta:
        db_table = "jmp_host"


class Track(models.Model):
    op_type_choices = (
        (1,'登录'),
        (2,'登出'),
        (3,'命令'),
    )
    op_state_choices = (
        (0, '执行成功'),
        (1, '执行发生错误'),
    )

    user = models.ForeignKey(User,models.PROTECT,db_column="user_id")
    host = models.ForeignKey("Host",models.PROTECT,db_column="host_id")
    source_ip = models.GenericIPAddressField()
    op_type = models.IntegerField(choices=op_type_choices)
    op_date = models.DateTimeField(auto_now_add=True)
    command = models.CharField(max_length=255,null=True,blank=True,verbose_name="命令")
    op_state = models.BooleanField(verbose_name="执行结果")
    class Meta:
        db_table = "jmp_track"