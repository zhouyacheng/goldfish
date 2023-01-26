from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class UserProfile(User):
    class Meta:
        db_table = "auth_userprofile"
        verbose_name = "用户信息表"
    phone = models.CharField(max_length=32,null=True,blank=True,verbose_name="电话号码")