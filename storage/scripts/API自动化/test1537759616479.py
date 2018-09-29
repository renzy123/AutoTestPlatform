from django.db import models


# Create your models here.

class Script(models.Model):
    """
    脚本的模型
    字段介绍：
    desc:脚本描述
    path:脚本路径
    create_time:创建时间
    create_user:创建用户
    run_count:执行次数统计
    last_run_time:上次执行时间
    related_case:关联测试用例
    last_edit_time:上次编辑时间
    last_edit_user:上次编辑用户
    """

    desc = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=100, null=False, default="")
    path = models.CharField(max_length=100, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.IntegerField()
    run_count = models.IntegerField(default=0)
    last_run_time = models.DateTimeField(null=True)
    related_case = models.IntegerField(null=True)
    last_edit_time = models.DateTimeField(auto_now=True)
    last_edit_user = models.IntegerField(null=True)
    script_type = models.IntegerField()


class ScriptType(models.Model):
    """
    脚本类型的模型
    desc:描述
    name:类型名称
    id:类型ID
    """
    desc = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)
