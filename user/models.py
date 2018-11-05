from django.db import models


# Create your models here.


class User(models.Model):
    """
    设置数据库
    name:用户名
    password:用户密码
    last_login_time:上一次登录时间
    create_time:首次登录时间
    privilege:权限
    id:自增主键
    """
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    last_login_time = models.DateTimeField()
    create_time = models.DateTimeField()
    privilege = models.IntegerField()
    default_mail = str(name) + "@mail.jj.cn"
    email = models.EmailField(default=default_mail, unique=True)
    id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=20, default="无")


class Privilege(models.Model):
    """
    设置数据库
    """
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
