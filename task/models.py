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
    status = models.IntegerField()
    product = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.IntegerField()
    desc = models.CharField(max_length=100)
    runtime = models.IntegerField(default=0)
    last_run_time = models.DateTimeField(null=True)



class TaskStatus(models.Model):
    """
    任务状态实体类，用于描述任务的状态
    title:状态名
    desc:状态描述
    """
    title = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=100, null=True)


class Result(models.Model):
    """执行结果类，用于记录任务执行的结果
    report_title:执行报告名
    log_title:日志目录
    task:任务名称
    """
    report_title = models.CharField(max_length=100)
    log_title = models.CharField(max_length=100)
    task = models.IntegerField()
    result = models.IntegerField(default=0)
    run_time = models.DateTimeField()
    run_user = models.IntegerField(default=0)


class TestResultType(models.Model):
    """测试结果的类型"""
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)


class TaskSuiteMapping(models.Model):
    """
    任务和测试套件的多对多的关系的隐射
    """
    task = models.IntegerField()
    suite = models.IntegerField()
