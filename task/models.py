from django.db import models


# Create your models here.

class TestTask(models.Model):
    """
    测试任务的模型
    字段说明：
    title:任务的标题
    create_time:任务的创建时间
    create_user:任务的创建者
    test_times:测试的执行次数
    """
    title = models.CharField(max_length=255)
    test_times = models.IntegerField()
    status = models.IntegerField()
    product = models.IntegerField()
    suit = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.IntegerField()
    desc = models.CharField(max_length=100)


class TaskStatus(models.Model):
    """
    任务状态实体类，用于描述任务的状态
    title:状态名
    desc:状态描述
    """
    title = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=100, null=True)
