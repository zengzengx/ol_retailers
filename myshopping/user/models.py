from django.db import models
from django.contrib.auth.models import User


class UserOther(models.Model):
    id = models.AutoField(primary_key=True)
    # 用户昵称
    nickname = models.CharField(max_length=255, unique=True, verbose_name='用户昵称')
    # 用户年龄
    age = models.IntegerField(default=18, verbose_name='用户年龄')
    # 用户性别
    gender = models.CharField(max_length=10, default='男', verbose_name="用户性别")
    # 用户头像
    header = models.ImageField(upload_to='static/images/header', default='static/images/header/default.jpg', verbose_name='用户头像')
    # 联系方式
    phone = models.CharField(max_length=50,default=110, verbose_name='用户手机')
    # 外键关联
    user = models.OneToOneField(User, on_delete=models.CASCADE)

